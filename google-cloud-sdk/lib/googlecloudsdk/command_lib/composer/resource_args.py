# Copyright 2018 Google Inc. All Rights Reserved.
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
"""Shared resource flags for Cloud Composer commands."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.calliope.concepts import concepts
from googlecloudsdk.calliope.concepts import deps
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.core import properties


def ProjectAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='project',
      help_text='The Cloud project for the {resource}.',
      fallthroughs=[deps.PropertyFallthrough(properties.VALUES.core.project)])


def LocationAttributeConfig(fallthroughs_enabled=True):
  fallthroughs = ([
      deps.PropertyFallthrough(properties.VALUES.composer.location)
  ] if fallthroughs_enabled else [])
  return concepts.ResourceParameterAttributeConfig(
      name='location',
      help_text='The Cloud location for the {resource}.',
      fallthroughs=fallthroughs)


def EnvironmentAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='environment',
      help_text='The Cloud Composer environment for the {resource}.')


def OperationAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='operation',
      help_text='The Cloud Composer operation for the {resource}.')


def GetLocationResourceSpec():
  return concepts.ResourceSpec(
      'composer.projects.locations',
      resource_name='location',
      projectsId=ProjectAttributeConfig(),
      locationsId=LocationAttributeConfig(fallthroughs_enabled=False))


def GetEnvironmentResourceSpec():
  return concepts.ResourceSpec(
      'composer.projects.locations.environments',
      resource_name='environment',
      projectsId=ProjectAttributeConfig(),
      locationsId=LocationAttributeConfig(),
      environmentsId=EnvironmentAttributeConfig())


def GetOperationResourceSpec():
  return concepts.ResourceSpec(
      'composer.projects.locations.operations',
      resource_name='operation',
      projectsId=ProjectAttributeConfig(),
      locationsId=LocationAttributeConfig(),
      operationsId=OperationAttributeConfig())


def AddLocationResourceArg(parser,
                           verb,
                           positional=True,
                           required=True,
                           plural=False):
  """Add a resource argument for a Cloud Composer location.

  NOTE: Must be used only if it's the only resource arg in the command.

  Args:
    parser: the parser for the command
    verb: str, the verb to describe the resource, for example, 'to update'.
    positional: boolean, if True, means that the resource is a positional rather
        than a flag.
    required: boolean, if True, the arg is required
    plural: boolean, if True, expects a list of resources
  """
  noun = 'location' + ('s' if plural else '')
  name = _BuildArgName(noun, positional)
  concept_parsers.ConceptParser.ForResource(
      name,
      GetLocationResourceSpec(),
      'The {} {}.'.format(noun, verb),
      required=required,
      plural=plural).AddToParser(parser)


def AddEnvironmentResourceArg(parser,
                              verb,
                              positional=True,
                              required=True,
                              plural=False):
  """Add a resource argument for a Cloud Composer Environment.

  NOTE: Must be used only if it's the only resource arg in the command.

  Args:
    parser: the parser for the command
    verb: str, the verb to describe the resource, for example, 'to update'.
    positional: boolean, if True, means that the resource is a positional rather
        than a flag.
    required: boolean, if True, the arg is required
    plural: boolean, if True, expects a list of resources
  """
  noun = 'environment' + ('s' if plural else '')
  name = _BuildArgName(noun, positional)
  concept_parsers.ConceptParser.ForResource(
      name,
      GetEnvironmentResourceSpec(),
      'The {} {}.'.format(noun, verb),
      required=required,
      plural=plural).AddToParser(parser)


def AddOperationResourceArg(parser,
                            verb,
                            positional=True,
                            required=True,
                            plural=False):
  """Add a resource argument for a Cloud Composer long-running operation.

  NOTE: Must be used only if it's the only resource arg in the command.

  Args:
    parser: the parser for the command
    verb: str, the verb to describe the resource, for example, 'to update'.
    positional: boolean, if True, means that the resource is a positional rather
        than a flag.
    required: boolean, if True, the arg is required
    plural: boolean, if True, expects a list of resources
  """
  noun = 'operation' + ('s' if plural else '')
  name = _BuildArgName(noun, positional)
  concept_parsers.ConceptParser.ForResource(
      name,
      GetOperationResourceSpec(),
      'The {} {}.'.format(noun, verb),
      required=required,
      plural=plural).AddToParser(parser)


def _BuildArgName(name, positional):
  return '{}{}'.format('' if positional else '--', name)
