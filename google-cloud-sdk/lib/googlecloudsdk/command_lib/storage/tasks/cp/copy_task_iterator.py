# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Task iterator for copy functionality."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.command_lib.storage import plurality_checkable_iterator
from googlecloudsdk.command_lib.storage import resource_reference
from googlecloudsdk.command_lib.storage import storage_url
from googlecloudsdk.command_lib.storage import wildcard_iterator
from googlecloudsdk.command_lib.storage.tasks.cp import copy_task_factory


class CopyTaskIterator:
  """Iterates over each expanded source and creates an appropriate copy task."""

  def __init__(self, source_name_iterator, destination_string):
    """Initializes a CopyTaskIterator instance.

    Args:
      source_name_iterator (name_expansion.NameExpansionIterator):
        yields resource_reference.Resource objects with expanded source urls.
      destination_string (str): The copy destination path/url.
    """
    self._source_name_iterator = (
        plurality_checkable_iterator.PluralityCheckableIterator(
            source_name_iterator))
    self._multiple_sources = self._source_name_iterator.is_plural()
    self._destination_string = destination_string

  def __iter__(self):
    raw_destination = self._get_raw_destination()
    for source_resource in self._source_name_iterator:
      destination_resource = self._get_copy_destination(raw_destination,
                                                        source_resource)
      yield copy_task_factory.get_copy_task(source_resource,
                                            destination_resource)

  def _get_raw_destination(self):
    """Converts self._destination_string to a destination resource.

    Returns:
      A resource_reference.Resource. Note that this resource may not be a valid
      copy destination if it is a BucketResource, PrefixResource,
      FileDirectoryResource or UnknownResource.

    Raises:
      ValueError if the destination url is a cloud provider or if it specifies
      a version.
    """
    destination_url = storage_url.storage_url_from_string(
        self._destination_string)

    if isinstance(destination_url, storage_url.CloudUrl):
      if destination_url.is_provider():
        raise ValueError(
            'The cp command does not support provider-only destination URLs.')
      elif destination_url.generation is not None:
        raise ValueError(
            'The destination argument of the cp command cannot be a '
            'version-specific URL ({}).'
            .format(self._destination_string))

    raw_destination = self._expand_destination_wildcards()
    if raw_destination:
      return raw_destination
    return resource_reference.UnknownResource(destination_url)

  def _expand_destination_wildcards(self):
    """Expands destination wildcards.

    Ensures that only one resource matches the wildcard expanded string. Much
    like the unix cp command, the storage surface only supports copy operations
    to one user-specified destination.

    Returns:
      A resource_reference.Resource, or None if no matching resource is found.

    Raises:
      ValueError if more than one resource is matched, or the source contained
      an unescaped wildcard and no resources were matched.
    """
    destination_iterator = (
        plurality_checkable_iterator.PluralityCheckableIterator(
            wildcard_iterator.get_wildcard_iterator(self._destination_string)))

    contains_unexpanded_wildcard = (
        destination_iterator.is_empty() and
        wildcard_iterator.contains_wildcard(self._destination_string))

    if destination_iterator.is_plural() or contains_unexpanded_wildcard:
      raise ValueError('Destination ({}) must match exactly one URL'.format(
          self._destination_string))

    if not destination_iterator.is_empty():
      return next(destination_iterator)

  def _get_copy_destination(self, raw_destination, source_resource):
    completion_is_necessary = (
        self._destination_is_container(raw_destination) or
        self._multiple_sources)

    if completion_is_necessary:
      return self._complete_destination(raw_destination, source_resource)
    else:
      return raw_destination

  def _destination_is_container(self, destination):
    try:
      return destination.is_container()
    except NotImplementedError:
      # Some resource classes are not clearly containers. In these cases we need
      # to use the storage_url attribute to infer how to treat them.
      destination_url = destination.storage_url
      return (
          destination_url.url_string.endswith(destination_url.delimiter) or (
              isinstance(destination_url, storage_url.CloudUrl) and
              destination_url.is_bucket()))

  def _complete_destination(self, destination_container, source_resource):
    """Gets a valid copy destination incorporating part of the source's name.

    When given a source file or object and a destination resource that should
    be treated as a container, this function uses the last part of the source's
    name to get an object or file resource representing the copy destination.

    For example: given a source `dir/file` and a destination `gs://bucket/`, the
    destination returned is a resource representing `gs://bucket/file`.

    Args:
      destination_container (resource_reference.Resource): The destination
        container.
      source_resource (resource_reference.Resource): The copy source.

    Returns:
      The completed destination, a resource_reference.Resource.
    """
    destination_url = destination_container.storage_url
    source_url = source_resource.storage_url

    container_string = storage_url.rstrip_one_delimiter(
        destination_url.url_string, delimiter=destination_url.delimiter)

    new_destination_string = (
        container_string +
        destination_url.delimiter +
        source_url.url_string.rpartition(source_url.delimiter)[2])

    new_destination_url = storage_url.storage_url_from_string(
        new_destination_string)
    return resource_reference.UnknownResource(new_destination_url)
