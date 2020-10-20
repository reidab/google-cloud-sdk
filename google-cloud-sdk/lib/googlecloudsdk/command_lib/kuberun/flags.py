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
"""Helpers to add flags to kuberun commands."""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import abc

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base

import six

_VISIBILITY_MODES = {
    'internal': 'Visible only within the cluster.',
    'external': 'Visible from outside the cluster.',
}


class BinaryCommandFlag(six.with_metaclass(abc.ABCMeta, object)):
  """Informal interface for flags that get passed through to an underlying binary."""

  @abc.abstractmethod
  def AddToParser(self, parser):
    """Adds this argument to the given parser.

    Args:
      parser: The argparse parser.
    """
    pass

  @abc.abstractmethod
  def FormatFlags(self, args):
    """Return flags in a format that can be passed to the underlying binary."""
    pass


class StringFlag(BinaryCommandFlag):
  """A flag that takes a string value that is just passed directly through to the binary."""

  def __init__(self, name, **kwargs):
    super(StringFlag, self).__init__()
    self.arg = base.Argument(name, **kwargs)

  def AddToParser(self, parser):
    return self.arg.AddToParser(parser)

  def FormatFlags(self, args):
    dest_name = _GetDestNameForFlag(self.arg.name)
    if args.IsSpecified(dest_name):
      return [self.arg.name, str(getattr(args, dest_name))]
    return []


class BooleanFlag(BinaryCommandFlag):
  """Encapsulates a boolean flag that can be either --<flag> or --no-<flag>."""

  def __init__(self, name, **kwargs):
    super(BooleanFlag, self).__init__()
    self.arg = base.Argument(
        name, action=arg_parsers.StoreTrueFalseAction, **kwargs)

  def AddToParser(self, parser):
    return self.arg.AddToParser(parser)

  def FormatFlags(self, args):
    base_flag = self.arg.name.replace('--', '')
    bool_flags = [self.arg.name, '--no-' + base_flag]
    return [f for f in bool_flags if f in args.GetSpecifiedArgNames()]


class BasicFlag(BinaryCommandFlag):
  """Encapsulates a flag that is passed through as-is when present."""

  def __init__(self, name, **kwargs):
    super(BasicFlag, self).__init__()
    self.arg = base.Argument(name, default=False, action='store_true', **kwargs)

  def AddToParser(self, parser):
    return self.arg.AddToParser(parser)

  def FormatFlags(self, args):
    dest_name = _GetDestNameForFlag(self.arg.name)
    if args.IsSpecified(dest_name):
      return [self.arg.name]
    return []


class FlagGroup(BinaryCommandFlag):
  """Encapsulates multiple flags that can't function independently."""

  def __init__(self, first, second, *args):
    """Create a new flag group.

    At least two flags must be specified.

    Args:
      first: the first flag in the group
      second: the second flag in the group
      *args: additional flags in the group
    """
    super(FlagGroup, self).__init__()
    all_flags = [first, second]
    all_flags.extend(args)
    self._flags = all_flags

  def AddToParser(self, parser):
    for f in self._flags:
      f.AddToParser(parser)

  def FormatFlags(self, args):
    all_flags = []
    for f in self._flags:
      all_flags.extend(f.FormatFlags(args))
    return all_flags


def NamespaceFlag():
  return StringFlag('--namespace', help='Kubernetes namespace to operate in.')


class NamespaceFlagGroup(BinaryCommandFlag):
  """Encapsulates logic for handling the mutually-exclusive flags --namespace and --all-namespaces."""

  def AddToParser(self, parser):
    mutex_group = parser.add_mutually_exclusive_group()
    NamespaceFlag().AddToParser(mutex_group)
    mutex_group.add_argument(
        '--all-namespaces',
        default=False,
        action='store_true',
        help='List the requested object(s) across all namespaces.')

  def FormatFlags(self, args):
    if args.IsSpecified('all_namespaces'):
      return ['--all-namespaces']
    return NamespaceFlag().FormatFlags(args)


class ClusterConnectionFlags(BinaryCommandFlag):
  """Encapsulates logic for handling flags used for connecting to a cluster."""

  def AddToParser(self, parser):
    mutex_group = parser.add_mutually_exclusive_group()
    gke_group = mutex_group.add_group()
    gke_group.add_argument(
        '--cluster',
        required=True,
        help='ID of the cluster or fully qualified identifier for the cluster. '
        'If specified, then --cluster-location is required. Cannot be '
        'specified together with --context and --kubeconfig.')
    gke_group.add_argument(
        '--cluster-location',
        required=True,
        help='Zone in which the cluster is located. If specified, then --cluster '
        'is required. Cannot be specified together with --context and '
        '--kubeconfig.')
    cluster_group = mutex_group.add_group()
    cluster_group.add_argument(
        '--context',
        help='Name of the context in your kubectl config file to use for '
        'connecting. Cannot be specified together with --cluster and '
        '--cluster-location.')
    cluster_group.add_argument(
        '--kubeconfig',
        help='Absolute path to your kubectl config file. If not specified, '
        'the colon- or semicolon-delimited list of paths specified by '
        '$KUBECONFIG will be used. If $KUBECONFIG is unset, this defaults to '
        '~/.kube/config. Cannot be specified together with --cluster and '
        '--cluster-location.')

  def FormatFlags(self, args):
    exec_args = []
    if args.IsSpecified('cluster'):
      exec_args.extend(['--cluster', args.cluster])
    if args.IsSpecified('cluster_location'):
      exec_args.extend(['--cluster-location', args.cluster_location])
    if args.IsSpecified('kubeconfig'):
      exec_args.extend(['--kubeconfig', args.kubeconfig])
    if args.IsSpecified('context'):
      exec_args.extend(['--context', args.context])
    return exec_args


class TrafficFlags(BinaryCommandFlag):
  """Encapsulates flags to configure traffic routes to the service."""

  def AddToParser(self, parser):
    mutex_group = parser.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument(
        '--to-latest',
        default=False,
        action='store_true',
        help='If true, assign 100 percent of traffic to the \'latest\' revision '
        'of this service. Note that when a new revision is created, it will '
        'become the \'latest\' and traffic will be directed to it. Defaults to '
        'False. Synonymous with `--to-revisions=LATEST=100`.')
    mutex_group.add_argument(
        '--to-revisions',
        help='Comma-separated list of traffic assignments in the form '
        'REVISION-NAME=PERCENTAGE. REVISION-NAME must be the name for a revision '
        'for the service as returned by \'gcloud kuberun core revisions list\'. '
        'PERCENTAGE must be an integer percentage between 0 and 100 inclusive. '
        'E.g. service-nw9hs=10,service-nw9hs=20 Up to 100 percent of traffic may '
        'be assigned. If 100 percent of traffic is assigned, the Service traffic '
        'is updated as specified. If under 100 percent of traffic is assigned, '
        'the Service traffic is updated as specified for revisions with '
        'assignments and traffic is scaled up or down down proportionally as '
        'needed for revision that are currently serving traffic but that do not '
        'have new assignments. For example assume revision-1 is serving 40 '
        'percent of traffic and revision-2 is serving 60 percent. If revision-1 '
        'is assigned 45 percent of traffic and no assignment is made for '
        'revision-2, the service is updated with revsion-1 assigned 45 percent '
        'of traffic and revision-2 scaled down to 55 percent. You can use '
        '"LATEST" as a special revision name to always put the given percentage '
        'of traffic on the latest ready revision.')

  def FormatFlags(self, args):
    if args.IsSpecified('to_latest'):
      return ['--to-latest']
    elif args.IsSpecified('to_revisions'):
      return ['--to-revisions', args.to_revisions]


def CommonServiceFlags(is_deploy=False):
  return FlagGroup(NamespaceFlag(), ImageFlag(required=is_deploy), CPUFlag(),
                   MemoryFlag(), PortFlag(), Http2Flag(), ConcurrencyFlag(),
                   EntrypointFlags(), ScalingFlags(), LabelsFlags(),
                   ConfigMapFlags(), SecretsFlags(), EnvVarsFlags(),
                   ConnectivityFlag(), ServiceAccountFlag(),
                   RevisionSuffixFlag(), TimeoutFlag())


def ImageFlag(required=False):
  return StringFlag(
      '--image',
      help='Name of the container image to deploy (e.g. gcr.io/cloudrun/hello:latest).',
      required=required)


def CPUFlag():
  return StringFlag(
      '--cpu',
      help='CPU limit, in Kubernetes cpu units, for the resource. Ex: .5, 500m, 2.'
  )


def MemoryFlag():
  return StringFlag(
      '--memory', help='Memory limit for the resource. Ex: 1Gi, 512Mi.')


def PortFlag():
  return StringFlag(
      '--port',
      help='Container port to receive requests at. Also sets the $PORT environment variable. Must be a number between 1 and 65535, inclusive. To unset this field, pass the special value "default".'
  )


def Http2Flag():
  return BooleanFlag(
      '--use-http2',
      help='If true, uses HTTP/2 for connections to the service.')


def ConcurrencyFlag():
  return StringFlag(
      '--concurrency',
      help='Maximum number of concurrent requests allowed per container instance. If concurrency is unspecified, any number of concurrent requests are allowed. To unset this field, provide the special value "default".'
  )


def EntrypointFlags():
  """Encapsulate flags for customizing container command."""
  args_flag = StringFlag(
      '--args',
      help='Comma-separated arguments passed to the command run by the '
      "container image. If not specified and no '--command' is provided, the "
      "container image's default Cmd is used. Otherwise, if not specified, no "
      'arguments are passed. To reset this field to its default, pass an empty '
      'string.')
  command_flag = StringFlag(
      '--command',
      help='Entrypoint for the container image. If not specified, the '
      "container image's default Entrypoint is run. To reset this field to its "
      'default, pass an empty string.')
  return FlagGroup(args_flag, command_flag)


def ScalingFlags():
  min_instances_flag = StringFlag(
      '--min-instances',
      help='Minimum number of container instances of the Service to run '
      "or 'default' to remove any minimum.")
  max_instances_flag = StringFlag(
      '--max-instances',
      help='Maximum number of container instances of the Service to run. '
      "Use 'default' to unset the limit and use the platform default.")
  return FlagGroup(min_instances_flag, max_instances_flag)


class LabelsFlags(BinaryCommandFlag):
  """Encapsulates flags to configure label of the service."""

  def AddToParser(self, parser):
    # TODO(b/166474467): revisit if no-opt flags should be kept for deploy
    mutex_group = parser.add_mutually_exclusive_group()
    mutex_group.add_argument(
        '--clear-labels',
        default=False,
        action='store_true',
        help='If true, removes all labels. If --update-labels is also specified then '
        '--clear-labels is applied first.')
    mutex_group.add_argument(
        '--labels',
        help='List of label KEY=VALUE pairs to add. An alias to --update-labels.'
    )
    update_group = mutex_group.add_group()
    update_group.add_argument(
        '--remove-labels',
        help='List of label keys to remove. If a label does not exist it is '
        'silently ignored. If --update-labels is also specified then '
        '--remove-labels is applied first.')
    update_group.add_argument(
        '--update-labels',
        help='List of label KEY=VALUE pairs to update. If a label exists its '
        'value is modified, otherwise a new label is created.')

  def FormatFlags(self, args):
    command_flags = []
    if args.IsSpecified('clear_labels'):
      command_flags.append('--clear-labels')
    if args.IsSpecified('labels'):
      command_flags.extend(['--labels', args.labels])
    if args.IsSpecified('remove_labels'):
      command_flags.extend(['--remove-labels', args.remove_labels])
    if args.IsSpecified('update_labels'):
      command_flags.extend(['--update-labels', args.update_labels])
    return command_flags


class ConfigMapFlags(BinaryCommandFlag):
  """Encapsulates flags to configure config maps mounting."""

  def AddToParser(self, parser):
    # TODO(b/166474467): revisit if no-opt flags should be kept for deploy
    mutex_group = parser.add_mutually_exclusive_group(
        help='Config map to mount or provide as environment variables. '
        "Keys starting with a forward slash '/' are mount paths. All other keys "
        'correspond to environment variables. The values associated with each of '
        'these should be in the form CONFIG_MAP_NAME:KEY_IN_CONFIG_MAP; you may '
        'omit the key within the config map to specify a mount of all keys '
        'within the config map. For example: '
        '`--update-config-maps=/my/path=myconfig,ENV=otherconfig:key.json` '
        "will create a volume with config map 'myconfig' and mount that volume "
        "at '/my/path'. Because no config map key was specified, all keys in "
        "'myconfig' will be included. An environment variable named ENV will "
        "also be created whose value is the value of 'key.json' in 'otherconfig'."
    )
    mutex_group.add_argument(
        '--clear-config-maps',
        default=False,
        action='store_true',
        help='If true, removes all config-maps.')
    mutex_group.add_argument(
        '--set-config-maps',
        help='List of key-value pairs to set as config-maps. All existing '
        'config-maps will be removed first.')
    update_group = mutex_group.add_group(
        help='Only --update-config-maps and --remove-config-maps can be used '
        'together. If both are specified, --remove-config-maps will be applied '
        'first.')
    update_group.add_argument(
        '--remove-config-maps', help='List of config-maps to be removed.')
    update_group.add_argument(
        '--update-config-maps',
        help='List of key-value pairs to set as config-maps.')

  def FormatFlags(self, args):
    command_flags = []
    if args.IsSpecified('clear_config_maps'):
      command_flags.append('--clear-config-maps')
    if args.IsSpecified('set_config_maps'):
      command_flags.extend(['--set-config-maps', args.set_config_maps])
    if args.IsSpecified('remove_config_maps'):
      command_flags.extend(['--remove-config-maps', args.remove_config_maps])
    if args.IsSpecified('update_config_maps'):
      command_flags.extend(['--update-config-maps', args.update_config_maps])
    return command_flags


class SecretsFlags(BinaryCommandFlag):
  """Encapsulates flags to configure secrets mounting."""

  def AddToParser(self, parser):
    # TODO(b/166474467): revisit if no-opt flags should be kept for deploy
    mutex_group = parser.add_mutually_exclusive_group(
        help='Secrets to mount or provide as environment variables. Keys '
        "starting with a forward slash '/' are mount paths. All other keys "
        'correspond to environment variables. The values associated with each '
        'of these should be in the form SECRET_NAME:KEY_IN_SECRET; you may omit '
        'the key within the secret to specify a mount of all keys within the '
        'secret. For example: '
        '`--update-secrets=/my/path=mysecret,ENV=othersecret:key.json` will '
        "create a volume with secret 'mysecret' and mount that volume at "
        "'/my/path'. Because no secret key was specified, all keys in 'mysecret' "
        'will be included. An environment variable named ENV will also be '
        "created whose value is the value of 'key.json' in 'othersecret'.")
    mutex_group.add_argument(
        '--clear-secrets',
        default=False,
        action='store_true',
        help='Remove all secrets.')
    mutex_group.add_argument(
        '--set-secrets',
        help='List of key-value pairs to set as secrets. All '
        'existing secrets will be removed first.')
    update_group = mutex_group.add_group(
        help='Only --update-secrets and --remove-secrets can be used together. '
        'If both are specified, --remove-secrets will be applied first.')
    update_group.add_argument(
        '--remove-secrets', help='List of secrets to be removed.')
    update_group.add_argument(
        '--update-secrets', help='List of key-value pairs to set as secrets.')

  def FormatFlags(self, args):
    command_flags = []
    if args.IsSpecified('clear_secrets'):
      command_flags.append('--clear-secrets')
    if args.IsSpecified('set_secrets'):
      command_flags.extend(['--set-secrets', args.set_secrets])
    if args.IsSpecified('remove_secrets'):
      command_flags.extend(['--remove-secrets', args.remove_secrets])
    if args.IsSpecified('update_secrets'):
      command_flags.extend(['--update-secrets', args.update_secrets])
    return command_flags


class EnvVarsFlags(BinaryCommandFlag):
  """Encapsulates flags to configure environment variables."""

  def AddToParser(self, parser):
    mutex_group = parser.add_mutually_exclusive_group()
    mutex_group.add_argument(
        '--clear-env-vars',
        default=False,
        action='store_true',
        help='If true, removes all environment variables.')
    mutex_group.add_argument(
        '--set-env-vars',
        help='List of key-value pairs to set as environment '
        'variables. All existing environment variables will be removed first.')
    update_group = mutex_group.add_group(
        help='Only --update-env-vars and --remove-env-vars can be used together. '
        'If both are specified, --remove-env-vars will be applied first.')
    update_group.add_argument(
        '--remove-env-vars',
        help='List of environment variables to be removed.')
    update_group.add_argument(
        '--update-env-vars',
        help='List of key-value pairs to set as environment variables.')

  def FormatFlags(self, args):
    command_flags = []
    if args.IsSpecified('clear_env_vars'):
      command_flags.append('--clear-env-vars')
    if args.IsSpecified('set_env_vars'):
      command_flags.extend(['--set-env-vars', args.set_env_vars])
    if args.IsSpecified('remove_env_vars'):
      command_flags.extend(['--remove-env-vars', args.remove_env_vars])
    if args.IsSpecified('update_env_vars'):
      command_flags.extend(['--update-env-vars', args.update_env_vars])
    return command_flags


def ConnectivityFlag():
  return StringFlag(
      '--connectivity',
      help='Defaults to \'external\'. If \'external\', the service can be '
      'invoked through the internet, in addition to through the cluster '
      'network.',
      choices=_VISIBILITY_MODES)


def NoTrafficFlag():
  return BasicFlag(
      '--no-traffic',
      help='If set, any traffic assigned to the LATEST revision will be '
      'assigned to the specific revision bound to LATEST before the '
      'deployment. This means the revision being deployed will not receive '
      'traffic. After a deployment with this flag, the LATEST revision will '
      'not receive traffic on future deployments.')


def ServiceAccountFlag():
  return StringFlag(
      '--service-account',
      help='Service account associated with the revision of the service. '
      'The service account represents the identity of the running revision, '
      'and determines what permissions the revision has. This is the name of '
      'a Kubernetes service account in the same namespace as the service. '
      'If not provided, the revision will use the default Kubernetes '
      'namespace service account.')


def TimeoutFlag():
  return StringFlag(
      '--timeout',
      help='Maximum request execution time (timeout). It is specified '
      'as a duration; for example, "10m5s" is ten minutes and five seconds. '
      'If you don\'t specify a unit, seconds is assumed. For example, "10" is '
      '10 seconds.',
      type=arg_parsers.Duration(lower_bound='1s', parsed_unit='s'))


def RevisionSuffixFlag():
  return StringFlag(
      '--revision-suffix',
      help='Suffix of the revision name. Revision names always start with the '
      'service name automatically. For example, specifying '
      "`--revision-suffix=v1` for a service named 'helloworld', would lead "
      "to a revision named 'helloworld-v1'.")


def AsyncFlag():
  return BasicFlag(
      '--async',
      help='Return immediately, without waiting for the operation in progress '
      'to complete.')


def RegisterFlags(parser, flags):
  """Helper to register a set of flags with a given parser."""
  for f in flags:
    f.AddToParser(parser)


def _GetDestNameForFlag(flag):
  return flag.replace('--', '').replace('-', '_')
