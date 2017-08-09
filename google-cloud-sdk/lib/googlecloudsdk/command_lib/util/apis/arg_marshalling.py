# Copyright 2016 Google Inc. All Rights Reserved.
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

"""Utilities related to adding flags for the gcloud meta api commands."""

import re

from apitools.base.protorpclite import messages

from googlecloudsdk.calliope import base
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources
from googlecloudsdk.core.resource import resource_property


_TYPES = {
    messages.Variant.DOUBLE: float,
    messages.Variant.FLOAT: float,

    messages.Variant.INT64: long,
    messages.Variant.UINT64: long,
    messages.Variant.SINT64: long,

    messages.Variant.INT32: int,
    messages.Variant.UINT32: int,
    messages.Variant.SINT32: int,

    messages.Variant.BOOL: bool,
    messages.Variant.STRING: str,

    # TODO(b/38000796): Do something with bytes.
    messages.Variant.BYTES: None,
    messages.Variant.ENUM: None,
    messages.Variant.MESSAGE: None,
}


# TODO(b/38000796): Use the same defaults as the normal resource parser.
DEFAULT_PARAMS = {
    'project': properties.VALUES.core.project.Get,
    'projectId': properties.VALUES.core.project.Get,
    'projectsId': properties.VALUES.core.project.Get,
}


class ArgumentGenerator(object):
  """Class to generate and parse argparse flags from apitools message fields."""
  FLAT_RESOURCE_ARG_NAME = 'resource'
  AUTO_RENAME_FIELDS = {'projectId': 'project',
                        'projectsId': 'project'}
  IGNORABLE_LIST_FIELDS = {'filter', 'pageToken', 'orderBy'}

  def __init__(self, method, arg_info=None, raw=False, clean_surface=False,
               is_positional=True):
    """Creates a new Argument Generator.

    Args:
      method: APIMethod, The method to generate arguments for.
      arg_info: {str: yaml_command_schema.Argument}, Optional information about
        request parameters and how to map them into arguments.
      raw: bool, True to do no special processing of arguments for list
        commands. If False, typical List command flags will be added in and the
        equivalent API fields will be ignored.
      clean_surface: bool, If true, we try to clean up the surface by making
        a few common transformations. This includes things like auto-renaming
        common fields (like projectsId) and naming the resource argument after
        the actual request field it represents instead of adding an additional
        'resource' argument. It also does not generate flags for atomic name
        fields for resources using that model. This only works if raw = False.
      is_positional: bool, True to make the resource argument positional, false
        if everything should be a flag. This only works if clean_surface = True.
    """
    self.method = method
    self.arg_info = arg_info or {}
    self.raw = raw
    self.clean_surface = not raw and clean_surface
    # You can't make a field into a positional if we are not flattening the
    # resource because there will be an extra 'resource' arg created.
    self.is_positional = self.clean_surface and is_positional
    self.is_atomic = self.method.detailed_params != self.method.params

    self.auto_rename_fields = dict()
    self.ignored_fields = set()
    if not raw:
      if self.clean_surface:
        self.auto_rename_fields.update(ArgumentGenerator.AUTO_RENAME_FIELDS)
      if self.method.IsPageableList():
        self.ignored_fields |= ArgumentGenerator.IGNORABLE_LIST_FIELDS
        batch_page_size_field = self.method.BatchPageSizeField()
        if batch_page_size_field:
          self.ignored_fields.add(batch_page_size_field)

  def GenerateArgs(self, include_global_list_flags=True):
    """Generates all the CLI arguments required to call this method.

    Args:
      include_global_list_flags: bool, True to generate flags for things like
        filter, sort-by, etc. This should be turned off if you are generating
        arguments into a command that is already a base.ListCommand and so will
        already have these common flags.

    Returns:
      {str, calliope.base.Action}, A map of field name to the argument.
    """
    args = {}
    if include_global_list_flags:
      args.update(self._GenerateListMethodFlags())
    args.update(self._GenerateMessageFieldsFlags(
        '', self.method.GetRequestType()))
    args.update(self._GenerateResourceArg())
    return args

  def CreateRequest(self, namespace):
    """Generates the request object for the method call from the parsed args.

    Args:
      namespace: The argparse namespace.

    Returns:
      The apitools message to be send to the method.
    """
    request_type = self.method.GetRequestType()
    # Recursively create the message and sub-messages.
    fields = self._ParseMessageFieldsFlags(namespace, '', request_type)

    # For each actual method path field, add the attribute to the request.
    ref = self._ParseResourceArg(namespace)
    if ref:
      relative_name = ref.RelativeName()
      fields.update(
          {f: getattr(ref, f, relative_name) for f in self.method.params})
    return request_type(**fields)

  def GetResponseResourceRef(self, id_value, namespace):
    parent_ref = self._ParseResourceArg(namespace)
    return resources.REGISTRY.Parse(
        id_value,
        collection=self.method.collection.full_name,
        params=parent_ref.AsDict())

  def _GenerateListMethodFlags(self):
    """Generates all the CLI flags for a List command.

    Returns:
      {str, calliope.base.Action}, A map of field name to the argument.
    """
    flags = {}
    if not self.raw and self.method.IsList():
      flags[base.FILTER_FLAG.name] = base.FILTER_FLAG
      flags[base.SORT_BY_FLAG.name] = base.SORT_BY_FLAG
      if self.method.IsPageableList() and self.method.ListItemField():
        # We can use YieldFromList() with a limit.
        flags[base.LIMIT_FLAG.name] = base.LIMIT_FLAG
        if self.method.BatchPageSizeField():
          # API supports page size.
          flags[base.PAGE_SIZE_FLAG.name] = base.PAGE_SIZE_FLAG
    return flags

  def Limit(self, namespace):
    """Gets the value of the limit flag (if present)."""
    if (not self.raw and
        self.method.IsPageableList() and
        self.method.ListItemField()):
      return getattr(namespace, 'limit')

  def PageSize(self, namespace):
    """Gets the value of the page size flag (if present)."""
    if (not self.raw and
        self.method.IsPageableList() and
        self.method.ListItemField() and
        self.method.BatchPageSizeField()):
      return getattr(namespace, 'page_size')

  def _GetRenamedField(self, field):
    i = self.arg_info.get(field)
    # Try to return an explicit override if it exists. If not, return an auto
    # rename or just the field itself.
    return i.arg_name if i else self.auto_rename_fields.get(field, field)

  def _GenerateResourceArg(self):
    """Gets the flags to add to the parser that appear in the method path.

    Returns:
      {str, calliope.base.Argument}, A map of field name to argument.
    """
    field_names = self.method.ResourceFieldNames()
    if not field_names:
      return {}

    message = self.method.GetRequestType()
    field_helps = _FieldHelpDocs(message)
    default_help = 'For substitution into: ' + self.method.detailed_path

    args = {}
    if not self.clean_surface:
      # Make a dedicated positional in addition to the flags for each part of
      # the URI path.
      args[ArgumentGenerator.FLAT_RESOURCE_ARG_NAME] = base.Argument(
          ArgumentGenerator.FLAT_RESOURCE_ARG_NAME,
          nargs='?',
          help='The GRI for the resource being operated on.')

    anchor_arg_name = self._GetRenamedField(field_names[-1])

    for param in field_names:
      data = self.arg_info.get(param)
      param = self._GetRenamedField(param)
      is_positional = (self.clean_surface and param == anchor_arg_name
                       and self.is_positional)
      args[param] = base.Argument(
          param if is_positional else '--' + param,
          metavar=resource_property.ConvertToAngrySnakeCase(param),
          # TODO(b/64147277): Usage a proper arg group to make the positional
          # and flags for the resource argument show up together.
          # category=(None if param == self.anchor_arg_name and
          # self.is_positional else 'RESOURCE'),
          type=str,
          completer=data.completer if data else None,
          help=data.help_text if data else field_helps.get(param, default_help))
      if (self.clean_surface and param == anchor_arg_name and
          not is_positional):
        args[param].kwargs['required'] = True
    return args

  def _ParseResourceArg(self, namespace):
    """Gets the resource ref for the resource specified as the positional arg.

    Args:
      namespace: The argparse namespace.

    Returns:
      The parsed resource ref or None if no resource arg was generated for this
      method.
    """
    field_names = self.method.ResourceFieldNames()
    if not field_names:
      return

    anchor_arg_name = self._GetRenamedField(field_names[-1])
    r = (getattr(namespace, anchor_arg_name) if self.clean_surface else
         getattr(namespace, ArgumentGenerator.FLAT_RESOURCE_ARG_NAME))

    params = {}
    for f in field_names:
      renamed = self._GetRenamedField(f)
      value = getattr(namespace, renamed)
      params[f] = value or DEFAULT_PARAMS.get(renamed, lambda: None)()

    return resources.REGISTRY.Parse(
        r,
        collection=self.method.RequestCollection().full_name,
        params=params)

  def _GenerateMessageFieldsFlags(self, prefix, message, is_root=True):
    """Gets the arguments to add to the parser that appear in the method body.

    Args:
      prefix: str, A string to prepend to the name of the flag. This is used
        for flags representing fields of a submessage.
      message: The apitools message to generate the flags for.
      is_root: bool, True if this is the request message itself (not a
        sub-field).

    Returns:
      {str, calliope.base.Argument}, A map of field name to argument.
    """
    args = {}
    field_helps = _FieldHelpDocs(message)
    for field in message.all_fields():
      name = self._FlagNameForField(prefix, field, is_root)
      if not name:
        continue
      if field.variant == messages.Variant.MESSAGE:
        field_help = field_helps.get(field.name, None)
        group = base.ArgumentGroup(
            name, description=(name + ': ' + field_help) if field_help else '')
        for arg in self._GenerateMessageFieldsFlags(
            name + '.', field.type, is_root=False).values():
          group.AddArgument(arg)
        args[name] = group
      else:
        args[name] = self._GenerateMessageFieldFlag(name, field, field_helps)
    return {k: v for k, v in args.iteritems() if v is not None}

  def _ParseMessageFieldsFlags(self, namespace, prefix, message, is_root=True):
    """Recursively generates the request message and any sub-messages.

    Args:
      namespace: The argparse namespace containing the all the parsed arguments.
      prefix: str, The flag prefix for the sub-message being generated.
      message: The apitools class for the message.
      is_root: bool, True if this is the request message itself (not a
        sub-field).

    Returns:
      The instantiated apitools Message with all fields filled in from flags.
    """
    kwargs = {}
    for field in message.all_fields():
      name = self._FlagNameForField(prefix, field, is_root)
      if not name:
        continue
      # Field is a sub-message, recursively generate it.
      if field.variant == messages.Variant.MESSAGE:
        sub_kwargs = self._ParseMessageFieldsFlags(
            namespace, name + '.', field.type, is_root=False)
        if sub_kwargs:
          # Only construct the sub-message if we have something to put in it.
          value = field.type(**sub_kwargs)
          # TODO(b/38000796): Handle repeated fields correctly.
          kwargs[field.name] = value if not field.repeated else [value]
      # Field is a scalar, just get the value.
      else:
        value = getattr(namespace, name, None)
        if value is not None:
          # TODO(b/38000796): Handle repeated fields correctly.
          kwargs[field.name] = value if not field.repeated else [value]
    return kwargs

  def _FlagNameForField(self, prefix, field, is_root):
    """Compute the flag name to generate for the given message field.

    Args:
      prefix: str, A prefix to put on the flag (when generating flags for
        sub-messages).
      field: MessageField, The apitools field to generate the flag for.
      is_root: bool, True if this is the request message itself (not a
        sub-field).

    Returns:
      str, The name of the flag to generate.
    """
    if self._ShouldSkipAtomicField(field, is_root):
      return None
    name = prefix + field.name
    name = self._GetRenamedField(name)
    if name in self.ignored_fields:
      return None
    if field.variant == messages.Variant.MESSAGE:
      if (name == self.method.request_field and
          name.lower().endswith('request')):
        name = 'request'
    return name

  def _ShouldSkipAtomicField(self, field, is_root):
    return (is_root and self.clean_surface and self.is_atomic
            and field.name in self.method.params)

  def _GenerateMessageFieldFlag(self, name, field, field_helps):
    """Gets a flag for a single field in a message.

    Args:
      name: The name of the field.
      field: The apitools field object.
      field_helps: {str: str}, A mapping of field name to help text.

    Returns:
      {str: str}, A mapping of field name to help text.
    """
    help_text = field_helps.get(field.name, None)
    if _IsOutputField(help_text):
      return None
    variant = field.variant
    t = _TYPES.get(variant, None)
    choices = None
    if variant == messages.Variant.ENUM:
      choices = field.type.names()
    return base.Argument(
        # TODO(b/38000796): Consider not using camel case for flags.
        '--' + name,
        metavar=resource_property.ConvertToAngrySnakeCase(field.name),
        category='MESSAGE',
        action='store',
        type=t,
        choices=choices,
        help=help_text,
    )


def _FieldHelpDocs(message):
  """Gets the help text for the fields in the request message.

  Args:
    message: The apitools message.

  Returns:
    {str: str}, A mapping of field name to help text.
  """
  field_helps = {}
  current_field = None

  match = re.search(r'^\s+Fields:.*$', message.__doc__, re.MULTILINE)
  if not match:
    # Couldn't find any fields at all.
    return field_helps

  for line in message.__doc__[match.end():].splitlines():
    match = re.match(r'^\s+(\w+): (.*)$', line)
    if match:
      # This line is the start of a new field.
      current_field = match.group(1)
      field_helps[current_field] = match.group(2).strip()
    elif current_field:
      # Append additional text to the in progress field.
      to_append = line.strip()
      if to_append:
        current_text = field_helps.get(current_field, '')
        field_helps[current_field] = current_text + ' ' + to_append

  return field_helps


def _IsOutputField(help_text):
  """Determines if the given field is output only based on help text."""
  return help_text and help_text.startswith('[Output Only]')
