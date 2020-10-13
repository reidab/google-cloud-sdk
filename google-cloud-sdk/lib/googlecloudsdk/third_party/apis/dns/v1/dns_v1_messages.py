"""Generated message classes for dns version v1.

Configures and serves authoritative DNS records.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'dns'


class Change(_messages.Message):
  r"""A Change object.

  Enums:
    StatusValueValuesEnum:

  Fields:
    additions: A ResourceRecordSet attribute.
    deletions: A ResourceRecordSet attribute.
    id: A string attribute.
    isServing: A boolean attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#change".
    startTime: A string attribute.
    status: A StatusValueValuesEnum attribute.
  """

  class StatusValueValuesEnum(_messages.Enum):
    r"""StatusValueValuesEnum enum type.

    Values:
      done: <no description>
      pending: <no description>
    """
    done = 0
    pending = 1

  additions = _messages.MessageField('ResourceRecordSet', 1, repeated=True)
  deletions = _messages.MessageField('ResourceRecordSet', 2, repeated=True)
  id = _messages.StringField(3)
  isServing = _messages.BooleanField(4)
  kind = _messages.StringField(5, default='dns#change')
  startTime = _messages.StringField(6)
  status = _messages.EnumField('StatusValueValuesEnum', 7)


class ChangesListResponse(_messages.Message):
  r"""A ChangesListResponse object.

  Fields:
    changes: A Change attribute.
    header: A ResponseHeader attribute.
    kind: Type of resource.
    nextPageToken: A string attribute.
  """

  changes = _messages.MessageField('Change', 1, repeated=True)
  header = _messages.MessageField('ResponseHeader', 2)
  kind = _messages.StringField(3, default='dns#changesListResponse')
  nextPageToken = _messages.StringField(4)


class DnsChangesCreateRequest(_messages.Message):
  r"""A DnsChangesCreateRequest object.

  Fields:
    change: A Change resource to be passed as the request body.
    clientOperationId: A string attribute.
    managedZone: A string attribute.
    project: A string attribute.
  """

  change = _messages.MessageField('Change', 1)
  clientOperationId = _messages.StringField(2)
  managedZone = _messages.StringField(3, required=True)
  project = _messages.StringField(4, required=True)


class DnsChangesGetRequest(_messages.Message):
  r"""A DnsChangesGetRequest object.

  Fields:
    changeId: A string attribute.
    clientOperationId: A string attribute.
    managedZone: A string attribute.
    project: A string attribute.
  """

  changeId = _messages.StringField(1, required=True)
  clientOperationId = _messages.StringField(2)
  managedZone = _messages.StringField(3, required=True)
  project = _messages.StringField(4, required=True)


class DnsChangesListRequest(_messages.Message):
  r"""A DnsChangesListRequest object.

  Enums:
    SortByValueValuesEnum:

  Fields:
    managedZone: A string attribute.
    maxResults: A integer attribute.
    pageToken: A string attribute.
    project: A string attribute.
    sortBy: A SortByValueValuesEnum attribute.
    sortOrder: A string attribute.
  """

  class SortByValueValuesEnum(_messages.Enum):
    r"""SortByValueValuesEnum enum type.

    Values:
      changeSequence: <no description>
    """
    changeSequence = 0

  managedZone = _messages.StringField(1, required=True)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  sortBy = _messages.EnumField('SortByValueValuesEnum', 5, default='changeSequence')
  sortOrder = _messages.StringField(6)


class DnsDnsKeysGetRequest(_messages.Message):
  r"""A DnsDnsKeysGetRequest object.

  Fields:
    clientOperationId: A string attribute.
    digestType: A string attribute.
    dnsKeyId: A string attribute.
    managedZone: A string attribute.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  digestType = _messages.StringField(2)
  dnsKeyId = _messages.StringField(3, required=True)
  managedZone = _messages.StringField(4, required=True)
  project = _messages.StringField(5, required=True)


class DnsDnsKeysListRequest(_messages.Message):
  r"""A DnsDnsKeysListRequest object.

  Fields:
    digestType: A string attribute.
    managedZone: A string attribute.
    maxResults: A integer attribute.
    pageToken: A string attribute.
    project: A string attribute.
  """

  digestType = _messages.StringField(1)
  managedZone = _messages.StringField(2, required=True)
  maxResults = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)


class DnsKey(_messages.Message):
  r"""A DnsKey object.

  Enums:
    AlgorithmValueValuesEnum:
    TypeValueValuesEnum:

  Fields:
    algorithm: A AlgorithmValueValuesEnum attribute.
    creationTime: A string attribute.
    description: A string attribute.
    digests: A DnsKeyDigest attribute.
    id: A string attribute.
    isActive: A boolean attribute.
    keyLength: A integer attribute.
    keyTag: A integer attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#dnsKey".
    publicKey: A string attribute.
    type: A TypeValueValuesEnum attribute.
  """

  class AlgorithmValueValuesEnum(_messages.Enum):
    r"""AlgorithmValueValuesEnum enum type.

    Values:
      ecdsap256sha256: <no description>
      ecdsap384sha384: <no description>
      rsasha1: <no description>
      rsasha256: <no description>
      rsasha512: <no description>
    """
    ecdsap256sha256 = 0
    ecdsap384sha384 = 1
    rsasha1 = 2
    rsasha256 = 3
    rsasha512 = 4

  class TypeValueValuesEnum(_messages.Enum):
    r"""TypeValueValuesEnum enum type.

    Values:
      keySigning: <no description>
      zoneSigning: <no description>
    """
    keySigning = 0
    zoneSigning = 1

  algorithm = _messages.EnumField('AlgorithmValueValuesEnum', 1)
  creationTime = _messages.StringField(2)
  description = _messages.StringField(3)
  digests = _messages.MessageField('DnsKeyDigest', 4, repeated=True)
  id = _messages.StringField(5)
  isActive = _messages.BooleanField(6)
  keyLength = _messages.IntegerField(7, variant=_messages.Variant.UINT32)
  keyTag = _messages.IntegerField(8, variant=_messages.Variant.INT32)
  kind = _messages.StringField(9, default='dns#dnsKey')
  publicKey = _messages.StringField(10)
  type = _messages.EnumField('TypeValueValuesEnum', 11)


class DnsKeyDigest(_messages.Message):
  r"""A DnsKeyDigest object.

  Enums:
    TypeValueValuesEnum:

  Fields:
    digest: A string attribute.
    type: A TypeValueValuesEnum attribute.
  """

  class TypeValueValuesEnum(_messages.Enum):
    r"""TypeValueValuesEnum enum type.

    Values:
      sha1: <no description>
      sha256: <no description>
      sha384: <no description>
    """
    sha1 = 0
    sha256 = 1
    sha384 = 2

  digest = _messages.StringField(1)
  type = _messages.EnumField('TypeValueValuesEnum', 2)


class DnsKeySpec(_messages.Message):
  r"""A DnsKeySpec object.

  Enums:
    AlgorithmValueValuesEnum:
    KeyTypeValueValuesEnum:

  Fields:
    algorithm: A AlgorithmValueValuesEnum attribute.
    keyLength: A integer attribute.
    keyType: A KeyTypeValueValuesEnum attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#dnsKeySpec".
  """

  class AlgorithmValueValuesEnum(_messages.Enum):
    r"""AlgorithmValueValuesEnum enum type.

    Values:
      ecdsap256sha256: <no description>
      ecdsap384sha384: <no description>
      rsasha1: <no description>
      rsasha256: <no description>
      rsasha512: <no description>
    """
    ecdsap256sha256 = 0
    ecdsap384sha384 = 1
    rsasha1 = 2
    rsasha256 = 3
    rsasha512 = 4

  class KeyTypeValueValuesEnum(_messages.Enum):
    r"""KeyTypeValueValuesEnum enum type.

    Values:
      keySigning: <no description>
      zoneSigning: <no description>
    """
    keySigning = 0
    zoneSigning = 1

  algorithm = _messages.EnumField('AlgorithmValueValuesEnum', 1)
  keyLength = _messages.IntegerField(2, variant=_messages.Variant.UINT32)
  keyType = _messages.EnumField('KeyTypeValueValuesEnum', 3)
  kind = _messages.StringField(4, default='dns#dnsKeySpec')


class DnsKeysListResponse(_messages.Message):
  r"""A DnsKeysListResponse object.

  Fields:
    dnsKeys: A DnsKey attribute.
    header: A ResponseHeader attribute.
    kind: Type of resource.
    nextPageToken: A string attribute.
  """

  dnsKeys = _messages.MessageField('DnsKey', 1, repeated=True)
  header = _messages.MessageField('ResponseHeader', 2)
  kind = _messages.StringField(3, default='dns#dnsKeysListResponse')
  nextPageToken = _messages.StringField(4)


class DnsManagedZoneOperationsGetRequest(_messages.Message):
  r"""A DnsManagedZoneOperationsGetRequest object.

  Fields:
    clientOperationId: A string attribute.
    managedZone: A string attribute.
    operation: A string attribute.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  managedZone = _messages.StringField(2, required=True)
  operation = _messages.StringField(3, required=True)
  project = _messages.StringField(4, required=True)


class DnsManagedZoneOperationsListRequest(_messages.Message):
  r"""A DnsManagedZoneOperationsListRequest object.

  Enums:
    SortByValueValuesEnum:

  Fields:
    managedZone: A string attribute.
    maxResults: A integer attribute.
    pageToken: A string attribute.
    project: A string attribute.
    sortBy: A SortByValueValuesEnum attribute.
  """

  class SortByValueValuesEnum(_messages.Enum):
    r"""SortByValueValuesEnum enum type.

    Values:
      id: <no description>
      startTime: <no description>
    """
    id = 0
    startTime = 1

  managedZone = _messages.StringField(1, required=True)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  sortBy = _messages.EnumField('SortByValueValuesEnum', 5, default='startTime')


class DnsManagedZonesCreateRequest(_messages.Message):
  r"""A DnsManagedZonesCreateRequest object.

  Fields:
    clientOperationId: A string attribute.
    managedZone: A ManagedZone resource to be passed as the request body.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  managedZone = _messages.MessageField('ManagedZone', 2)
  project = _messages.StringField(3, required=True)


class DnsManagedZonesDeleteRequest(_messages.Message):
  r"""A DnsManagedZonesDeleteRequest object.

  Fields:
    clientOperationId: A string attribute.
    managedZone: A string attribute.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  managedZone = _messages.StringField(2, required=True)
  project = _messages.StringField(3, required=True)


class DnsManagedZonesDeleteResponse(_messages.Message):
  r"""An empty DnsManagedZonesDelete response."""


class DnsManagedZonesGetRequest(_messages.Message):
  r"""A DnsManagedZonesGetRequest object.

  Fields:
    clientOperationId: A string attribute.
    managedZone: A string attribute.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  managedZone = _messages.StringField(2, required=True)
  project = _messages.StringField(3, required=True)


class DnsManagedZonesListRequest(_messages.Message):
  r"""A DnsManagedZonesListRequest object.

  Fields:
    dnsName: A string attribute.
    maxResults: A integer attribute.
    pageToken: A string attribute.
    project: A string attribute.
  """

  dnsName = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)


class DnsManagedZonesPatchRequest(_messages.Message):
  r"""A DnsManagedZonesPatchRequest object.

  Fields:
    clientOperationId: A string attribute.
    managedZone: A string attribute.
    managedZoneResource: A ManagedZone resource to be passed as the request
      body.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  managedZone = _messages.StringField(2, required=True)
  managedZoneResource = _messages.MessageField('ManagedZone', 3)
  project = _messages.StringField(4, required=True)


class DnsManagedZonesUpdateRequest(_messages.Message):
  r"""A DnsManagedZonesUpdateRequest object.

  Fields:
    clientOperationId: A string attribute.
    managedZone: A string attribute.
    managedZoneResource: A ManagedZone resource to be passed as the request
      body.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  managedZone = _messages.StringField(2, required=True)
  managedZoneResource = _messages.MessageField('ManagedZone', 3)
  project = _messages.StringField(4, required=True)


class DnsPoliciesCreateRequest(_messages.Message):
  r"""A DnsPoliciesCreateRequest object.

  Fields:
    clientOperationId: A string attribute.
    policy: A Policy resource to be passed as the request body.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  policy = _messages.MessageField('Policy', 2)
  project = _messages.StringField(3, required=True)


class DnsPoliciesDeleteRequest(_messages.Message):
  r"""A DnsPoliciesDeleteRequest object.

  Fields:
    clientOperationId: A string attribute.
    policy: A string attribute.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  policy = _messages.StringField(2, required=True)
  project = _messages.StringField(3, required=True)


class DnsPoliciesDeleteResponse(_messages.Message):
  r"""An empty DnsPoliciesDelete response."""


class DnsPoliciesGetRequest(_messages.Message):
  r"""A DnsPoliciesGetRequest object.

  Fields:
    clientOperationId: A string attribute.
    policy: A string attribute.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  policy = _messages.StringField(2, required=True)
  project = _messages.StringField(3, required=True)


class DnsPoliciesListRequest(_messages.Message):
  r"""A DnsPoliciesListRequest object.

  Fields:
    maxResults: A integer attribute.
    pageToken: A string attribute.
    project: A string attribute.
  """

  maxResults = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  project = _messages.StringField(3, required=True)


class DnsPoliciesPatchRequest(_messages.Message):
  r"""A DnsPoliciesPatchRequest object.

  Fields:
    clientOperationId: A string attribute.
    policy: A string attribute.
    policyResource: A Policy resource to be passed as the request body.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  policy = _messages.StringField(2, required=True)
  policyResource = _messages.MessageField('Policy', 3)
  project = _messages.StringField(4, required=True)


class DnsPoliciesUpdateRequest(_messages.Message):
  r"""A DnsPoliciesUpdateRequest object.

  Fields:
    clientOperationId: A string attribute.
    policy: A string attribute.
    policyResource: A Policy resource to be passed as the request body.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  policy = _messages.StringField(2, required=True)
  policyResource = _messages.MessageField('Policy', 3)
  project = _messages.StringField(4, required=True)


class DnsProjectsGetRequest(_messages.Message):
  r"""A DnsProjectsGetRequest object.

  Fields:
    clientOperationId: A string attribute.
    project: A string attribute.
  """

  clientOperationId = _messages.StringField(1)
  project = _messages.StringField(2, required=True)


class DnsResourceRecordSetsListRequest(_messages.Message):
  r"""A DnsResourceRecordSetsListRequest object.

  Fields:
    managedZone: A string attribute.
    maxResults: A integer attribute.
    name: A string attribute.
    pageToken: A string attribute.
    project: A string attribute.
    type: A string attribute.
  """

  managedZone = _messages.StringField(1, required=True)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  name = _messages.StringField(3)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)
  type = _messages.StringField(6)


class ManagedZone(_messages.Message):
  r"""A ManagedZone object.

  Enums:
    VisibilityValueValuesEnum:

  Messages:
    LabelsValue: A LabelsValue object.

  Fields:
    creationTime: A string attribute.
    description: A string attribute.
    dnsName: A string attribute.
    dnssecConfig: A ManagedZoneDnsSecConfig attribute.
    forwardingConfig: A ManagedZoneForwardingConfig attribute.
    id: A string attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZone".
    labels: A LabelsValue attribute.
    name: A string attribute.
    nameServerSet: A string attribute.
    nameServers: A string attribute.
    peeringConfig: A ManagedZonePeeringConfig attribute.
    privateVisibilityConfig: A ManagedZonePrivateVisibilityConfig attribute.
    reverseLookupConfig: A ManagedZoneReverseLookupConfig attribute.
    visibility: A VisibilityValueValuesEnum attribute.
  """

  class VisibilityValueValuesEnum(_messages.Enum):
    r"""VisibilityValueValuesEnum enum type.

    Values:
      private: <no description>
      public: <no description>
    """
    private = 0
    public = 1

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""A LabelsValue object.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  creationTime = _messages.StringField(1)
  description = _messages.StringField(2)
  dnsName = _messages.StringField(3)
  dnssecConfig = _messages.MessageField('ManagedZoneDnsSecConfig', 4)
  forwardingConfig = _messages.MessageField('ManagedZoneForwardingConfig', 5)
  id = _messages.IntegerField(6, variant=_messages.Variant.UINT64)
  kind = _messages.StringField(7, default='dns#managedZone')
  labels = _messages.MessageField('LabelsValue', 8)
  name = _messages.StringField(9)
  nameServerSet = _messages.StringField(10)
  nameServers = _messages.StringField(11, repeated=True)
  peeringConfig = _messages.MessageField('ManagedZonePeeringConfig', 12)
  privateVisibilityConfig = _messages.MessageField('ManagedZonePrivateVisibilityConfig', 13)
  reverseLookupConfig = _messages.MessageField('ManagedZoneReverseLookupConfig', 14)
  visibility = _messages.EnumField('VisibilityValueValuesEnum', 15)


class ManagedZoneDnsSecConfig(_messages.Message):
  r"""A ManagedZoneDnsSecConfig object.

  Enums:
    NonExistenceValueValuesEnum:
    StateValueValuesEnum:

  Fields:
    defaultKeySpecs: A DnsKeySpec attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZoneDnsSecConfig".
    nonExistence: A NonExistenceValueValuesEnum attribute.
    state: A StateValueValuesEnum attribute.
  """

  class NonExistenceValueValuesEnum(_messages.Enum):
    r"""NonExistenceValueValuesEnum enum type.

    Values:
      nsec: <no description>
      nsec3: <no description>
    """
    nsec = 0
    nsec3 = 1

  class StateValueValuesEnum(_messages.Enum):
    r"""StateValueValuesEnum enum type.

    Values:
      off: <no description>
      on: <no description>
      transfer: <no description>
    """
    off = 0
    on = 1
    transfer = 2

  defaultKeySpecs = _messages.MessageField('DnsKeySpec', 1, repeated=True)
  kind = _messages.StringField(2, default='dns#managedZoneDnsSecConfig')
  nonExistence = _messages.EnumField('NonExistenceValueValuesEnum', 3)
  state = _messages.EnumField('StateValueValuesEnum', 4)


class ManagedZoneForwardingConfig(_messages.Message):
  r"""A ManagedZoneForwardingConfig object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZoneForwardingConfig".
    targetNameServers: A ManagedZoneForwardingConfigNameServerTarget
      attribute.
  """

  kind = _messages.StringField(1, default='dns#managedZoneForwardingConfig')
  targetNameServers = _messages.MessageField('ManagedZoneForwardingConfigNameServerTarget', 2, repeated=True)


class ManagedZoneForwardingConfigNameServerTarget(_messages.Message):
  r"""A ManagedZoneForwardingConfigNameServerTarget object.

  Enums:
    ForwardingPathValueValuesEnum:

  Fields:
    forwardingPath: A ForwardingPathValueValuesEnum attribute.
    ipv4Address: A string attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZoneForwardingConfigNameServerTarget".
  """

  class ForwardingPathValueValuesEnum(_messages.Enum):
    r"""ForwardingPathValueValuesEnum enum type.

    Values:
      default: <no description>
      private: <no description>
    """
    default = 0
    private = 1

  forwardingPath = _messages.EnumField('ForwardingPathValueValuesEnum', 1)
  ipv4Address = _messages.StringField(2)
  kind = _messages.StringField(3, default='dns#managedZoneForwardingConfigNameServerTarget')


class ManagedZoneOperationsListResponse(_messages.Message):
  r"""A ManagedZoneOperationsListResponse object.

  Fields:
    header: A ResponseHeader attribute.
    kind: Type of resource.
    nextPageToken: A string attribute.
    operations: A Operation attribute.
  """

  header = _messages.MessageField('ResponseHeader', 1)
  kind = _messages.StringField(2, default='dns#managedZoneOperationsListResponse')
  nextPageToken = _messages.StringField(3)
  operations = _messages.MessageField('Operation', 4, repeated=True)


class ManagedZonePeeringConfig(_messages.Message):
  r"""A ManagedZonePeeringConfig object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZonePeeringConfig".
    targetNetwork: A ManagedZonePeeringConfigTargetNetwork attribute.
  """

  kind = _messages.StringField(1, default='dns#managedZonePeeringConfig')
  targetNetwork = _messages.MessageField('ManagedZonePeeringConfigTargetNetwork', 2)


class ManagedZonePeeringConfigTargetNetwork(_messages.Message):
  r"""A ManagedZonePeeringConfigTargetNetwork object.

  Fields:
    deactivateTime: A string attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZonePeeringConfigTargetNetwork".
    networkUrl: A string attribute.
  """

  deactivateTime = _messages.StringField(1)
  kind = _messages.StringField(2, default='dns#managedZonePeeringConfigTargetNetwork')
  networkUrl = _messages.StringField(3)


class ManagedZonePrivateVisibilityConfig(_messages.Message):
  r"""A ManagedZonePrivateVisibilityConfig object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZonePrivateVisibilityConfig".
    networks: A ManagedZonePrivateVisibilityConfigNetwork attribute.
  """

  kind = _messages.StringField(1, default='dns#managedZonePrivateVisibilityConfig')
  networks = _messages.MessageField('ManagedZonePrivateVisibilityConfigNetwork', 2, repeated=True)


class ManagedZonePrivateVisibilityConfigNetwork(_messages.Message):
  r"""A ManagedZonePrivateVisibilityConfigNetwork object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZonePrivateVisibilityConfigNetwork".
    networkUrl: A string attribute.
  """

  kind = _messages.StringField(1, default='dns#managedZonePrivateVisibilityConfigNetwork')
  networkUrl = _messages.StringField(2)


class ManagedZoneReverseLookupConfig(_messages.Message):
  r"""A ManagedZoneReverseLookupConfig object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZoneReverseLookupConfig".
  """

  kind = _messages.StringField(1, default='dns#managedZoneReverseLookupConfig')


class ManagedZonesListResponse(_messages.Message):
  r"""A ManagedZonesListResponse object.

  Fields:
    header: A ResponseHeader attribute.
    kind: Type of resource.
    managedZones: A ManagedZone attribute.
    nextPageToken: A string attribute.
  """

  header = _messages.MessageField('ResponseHeader', 1)
  kind = _messages.StringField(2, default='dns#managedZonesListResponse')
  managedZones = _messages.MessageField('ManagedZone', 3, repeated=True)
  nextPageToken = _messages.StringField(4)


class Operation(_messages.Message):
  r"""A Operation object.

  Enums:
    StatusValueValuesEnum:

  Fields:
    dnsKeyContext: A OperationDnsKeyContext attribute.
    id: A string attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#operation".
    startTime: A string attribute.
    status: A StatusValueValuesEnum attribute.
    type: A string attribute.
    user: A string attribute.
    zoneContext: A OperationManagedZoneContext attribute.
  """

  class StatusValueValuesEnum(_messages.Enum):
    r"""StatusValueValuesEnum enum type.

    Values:
      done: <no description>
      pending: <no description>
    """
    done = 0
    pending = 1

  dnsKeyContext = _messages.MessageField('OperationDnsKeyContext', 1)
  id = _messages.StringField(2)
  kind = _messages.StringField(3, default='dns#operation')
  startTime = _messages.StringField(4)
  status = _messages.EnumField('StatusValueValuesEnum', 5)
  type = _messages.StringField(6)
  user = _messages.StringField(7)
  zoneContext = _messages.MessageField('OperationManagedZoneContext', 8)


class OperationDnsKeyContext(_messages.Message):
  r"""A OperationDnsKeyContext object.

  Fields:
    newValue: A DnsKey attribute.
    oldValue: A DnsKey attribute.
  """

  newValue = _messages.MessageField('DnsKey', 1)
  oldValue = _messages.MessageField('DnsKey', 2)


class OperationManagedZoneContext(_messages.Message):
  r"""A OperationManagedZoneContext object.

  Fields:
    newValue: A ManagedZone attribute.
    oldValue: A ManagedZone attribute.
  """

  newValue = _messages.MessageField('ManagedZone', 1)
  oldValue = _messages.MessageField('ManagedZone', 2)


class PoliciesListResponse(_messages.Message):
  r"""A PoliciesListResponse object.

  Fields:
    header: A ResponseHeader attribute.
    kind: Type of resource.
    nextPageToken: A string attribute.
    policies: A Policy attribute.
  """

  header = _messages.MessageField('ResponseHeader', 1)
  kind = _messages.StringField(2, default='dns#policiesListResponse')
  nextPageToken = _messages.StringField(3)
  policies = _messages.MessageField('Policy', 4, repeated=True)


class PoliciesPatchResponse(_messages.Message):
  r"""A PoliciesPatchResponse object.

  Fields:
    header: A ResponseHeader attribute.
    policy: A Policy attribute.
  """

  header = _messages.MessageField('ResponseHeader', 1)
  policy = _messages.MessageField('Policy', 2)


class PoliciesUpdateResponse(_messages.Message):
  r"""A PoliciesUpdateResponse object.

  Fields:
    header: A ResponseHeader attribute.
    policy: A Policy attribute.
  """

  header = _messages.MessageField('ResponseHeader', 1)
  policy = _messages.MessageField('Policy', 2)


class Policy(_messages.Message):
  r"""A Policy object.

  Fields:
    alternativeNameServerConfig: A PolicyAlternativeNameServerConfig
      attribute.
    description: A string attribute.
    enableInboundForwarding: A boolean attribute.
    enableLogging: A boolean attribute.
    id: A string attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#policy".
    name: A string attribute.
    networks: A PolicyNetwork attribute.
  """

  alternativeNameServerConfig = _messages.MessageField('PolicyAlternativeNameServerConfig', 1)
  description = _messages.StringField(2)
  enableInboundForwarding = _messages.BooleanField(3)
  enableLogging = _messages.BooleanField(4)
  id = _messages.IntegerField(5, variant=_messages.Variant.UINT64)
  kind = _messages.StringField(6, default='dns#policy')
  name = _messages.StringField(7)
  networks = _messages.MessageField('PolicyNetwork', 8, repeated=True)


class PolicyAlternativeNameServerConfig(_messages.Message):
  r"""A PolicyAlternativeNameServerConfig object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#policyAlternativeNameServerConfig".
    targetNameServers: A PolicyAlternativeNameServerConfigTargetNameServer
      attribute.
  """

  kind = _messages.StringField(1, default='dns#policyAlternativeNameServerConfig')
  targetNameServers = _messages.MessageField('PolicyAlternativeNameServerConfigTargetNameServer', 2, repeated=True)


class PolicyAlternativeNameServerConfigTargetNameServer(_messages.Message):
  r"""A PolicyAlternativeNameServerConfigTargetNameServer object.

  Enums:
    ForwardingPathValueValuesEnum:

  Fields:
    forwardingPath: A ForwardingPathValueValuesEnum attribute.
    ipv4Address: A string attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#policyAlternativeNameServerConfigTargetNameServer".
  """

  class ForwardingPathValueValuesEnum(_messages.Enum):
    r"""ForwardingPathValueValuesEnum enum type.

    Values:
      default: <no description>
      private: <no description>
    """
    default = 0
    private = 1

  forwardingPath = _messages.EnumField('ForwardingPathValueValuesEnum', 1)
  ipv4Address = _messages.StringField(2)
  kind = _messages.StringField(3, default='dns#policyAlternativeNameServerConfigTargetNameServer')


class PolicyNetwork(_messages.Message):
  r"""A PolicyNetwork object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#policyNetwork".
    networkUrl: A string attribute.
  """

  kind = _messages.StringField(1, default='dns#policyNetwork')
  networkUrl = _messages.StringField(2)


class Project(_messages.Message):
  r"""A Project object.

  Fields:
    id: A string attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#project".
    number: A string attribute.
    quota: A Quota attribute.
  """

  id = _messages.StringField(1)
  kind = _messages.StringField(2, default='dns#project')
  number = _messages.IntegerField(3, variant=_messages.Variant.UINT64)
  quota = _messages.MessageField('Quota', 4)


class Quota(_messages.Message):
  r"""A Quota object.

  Fields:
    allowManualDnssec: A boolean attribute.
    dnsKeysPerManagedZone: A integer attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#quota".
    managedZones: A integer attribute.
    managedZonesPerNetwork: A integer attribute.
    networksPerManagedZone: A integer attribute.
    networksPerPolicy: A integer attribute.
    policies: A integer attribute.
    resourceRecordsPerRrset: A integer attribute.
    rrsetAdditionsPerChange: A integer attribute.
    rrsetDeletionsPerChange: A integer attribute.
    rrsetsPerManagedZone: A integer attribute.
    targetNameServersPerManagedZone: A integer attribute.
    targetNameServersPerPolicy: A integer attribute.
    totalRrdataSizePerChange: A integer attribute.
    whitelistedKeySpecs: A DnsKeySpec attribute.
  """

  allowManualDnssec = _messages.BooleanField(1)
  dnsKeysPerManagedZone = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  kind = _messages.StringField(3, default='dns#quota')
  managedZones = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  managedZonesPerNetwork = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  networksPerManagedZone = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  networksPerPolicy = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  policies = _messages.IntegerField(8, variant=_messages.Variant.INT32)
  resourceRecordsPerRrset = _messages.IntegerField(9, variant=_messages.Variant.INT32)
  rrsetAdditionsPerChange = _messages.IntegerField(10, variant=_messages.Variant.INT32)
  rrsetDeletionsPerChange = _messages.IntegerField(11, variant=_messages.Variant.INT32)
  rrsetsPerManagedZone = _messages.IntegerField(12, variant=_messages.Variant.INT32)
  targetNameServersPerManagedZone = _messages.IntegerField(13, variant=_messages.Variant.INT32)
  targetNameServersPerPolicy = _messages.IntegerField(14, variant=_messages.Variant.INT32)
  totalRrdataSizePerChange = _messages.IntegerField(15, variant=_messages.Variant.INT32)
  whitelistedKeySpecs = _messages.MessageField('DnsKeySpec', 16, repeated=True)


class RRSetRoutingPolicy(_messages.Message):
  r"""A RRSetRoutingPolicy object.

  Fields:
    geoPolicy: A RRSetRoutingPolicyGeoPolicy attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#rRSetRoutingPolicy".
    wrrPolicy: A RRSetRoutingPolicyWrrPolicy attribute.
  """

  geoPolicy = _messages.MessageField('RRSetRoutingPolicyGeoPolicy', 1)
  kind = _messages.StringField(2, default='dns#rRSetRoutingPolicy')
  wrrPolicy = _messages.MessageField('RRSetRoutingPolicyWrrPolicy', 3)


class RRSetRoutingPolicyGeoPolicy(_messages.Message):
  r"""A RRSetRoutingPolicyGeoPolicy object.

  Fields:
    failovers: A RRSetRoutingPolicyGeoPolicyGeoPolicyItem attribute.
    items: A RRSetRoutingPolicyGeoPolicyGeoPolicyItem attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#rRSetRoutingPolicyGeoPolicy".
  """

  failovers = _messages.MessageField('RRSetRoutingPolicyGeoPolicyGeoPolicyItem', 1, repeated=True)
  items = _messages.MessageField('RRSetRoutingPolicyGeoPolicyGeoPolicyItem', 2, repeated=True)
  kind = _messages.StringField(3, default='dns#rRSetRoutingPolicyGeoPolicy')


class RRSetRoutingPolicyGeoPolicyGeoPolicyItem(_messages.Message):
  r"""A RRSetRoutingPolicyGeoPolicyGeoPolicyItem object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem".
    location: A string attribute.
    rrdatas: A string attribute.
    signatureRrdatas: A string attribute.
  """

  kind = _messages.StringField(1, default='dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem')
  location = _messages.StringField(2)
  rrdatas = _messages.StringField(3, repeated=True)
  signatureRrdatas = _messages.StringField(4, repeated=True)


class RRSetRoutingPolicyWrrPolicy(_messages.Message):
  r"""A RRSetRoutingPolicyWrrPolicy object.

  Fields:
    items: A RRSetRoutingPolicyWrrPolicyWrrPolicyItem attribute.
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#rRSetRoutingPolicyWrrPolicy".
  """

  items = _messages.MessageField('RRSetRoutingPolicyWrrPolicyWrrPolicyItem', 1, repeated=True)
  kind = _messages.StringField(2, default='dns#rRSetRoutingPolicyWrrPolicy')


class RRSetRoutingPolicyWrrPolicyWrrPolicyItem(_messages.Message):
  r"""A RRSetRoutingPolicyWrrPolicyWrrPolicyItem object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem".
    rrdatas: A string attribute.
    signatureRrdatas: A string attribute.
    weight: A number attribute.
  """

  kind = _messages.StringField(1, default='dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem')
  rrdatas = _messages.StringField(2, repeated=True)
  signatureRrdatas = _messages.StringField(3, repeated=True)
  weight = _messages.FloatField(4)


class ResourceRecordSet(_messages.Message):
  r"""A ResourceRecordSet object.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#resourceRecordSet".
    name: A string attribute.
    routingPolicy: A RRSetRoutingPolicy attribute.
    rrdatas: A string attribute.
    signatureRrdatas: A string attribute.
    ttl: A integer attribute.
    type: A string attribute.
  """

  kind = _messages.StringField(1, default='dns#resourceRecordSet')
  name = _messages.StringField(2)
  routingPolicy = _messages.MessageField('RRSetRoutingPolicy', 3)
  rrdatas = _messages.StringField(4, repeated=True)
  signatureRrdatas = _messages.StringField(5, repeated=True)
  ttl = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  type = _messages.StringField(7)


class ResourceRecordSetsListResponse(_messages.Message):
  r"""A ResourceRecordSetsListResponse object.

  Fields:
    header: A ResponseHeader attribute.
    kind: Type of resource.
    nextPageToken: A string attribute.
    rrsets: A ResourceRecordSet attribute.
  """

  header = _messages.MessageField('ResponseHeader', 1)
  kind = _messages.StringField(2, default='dns#resourceRecordSetsListResponse')
  nextPageToken = _messages.StringField(3)
  rrsets = _messages.MessageField('ResourceRecordSet', 4, repeated=True)


class ResponseHeader(_messages.Message):
  r"""A ResponseHeader object.

  Fields:
    operationId: A string attribute.
  """

  operationId = _messages.StringField(1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: An opaque string that represents a user for quota purposes.
      Must not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    userIp: Deprecated. Please use quotaUser instead.
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = _messages.EnumField('AltValueValuesEnum', 1, default='json')
  fields = _messages.StringField(2)
  key = _messages.StringField(3)
  oauth_token = _messages.StringField(4)
  prettyPrint = _messages.BooleanField(5, default=True)
  quotaUser = _messages.StringField(6)
  trace = _messages.StringField(7)
  userIp = _messages.StringField(8)


