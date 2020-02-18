"""Generated client library for secretmanager version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.secretmanager.v1beta1 import secretmanager_v1beta1_messages as messages


class SecretmanagerV1beta1(base_api.BaseApiClient):
  """Generated client library for service secretmanager version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://secretmanager.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'secretmanager'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'SecretmanagerV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new secretmanager handle."""
    url = url or self.BASE_URL
    super(SecretmanagerV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects_secrets_versions = self.ProjectsSecretsVersionsService(self)
    self.projects_secrets = self.ProjectsSecretsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(SecretmanagerV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (SecretmanagerProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'secretmanager.projects.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'SecretmanagerProjectsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (SecretmanagerProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations',
        http_method=u'GET',
        method_id=u'secretmanager.projects.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+name}/locations',
        request_field='',
        request_type_name=u'SecretmanagerProjectsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsSecretsVersionsService(base_api.BaseApiService):
    """Service class for the projects_secrets_versions resource."""

    _NAME = u'projects_secrets_versions'

    def __init__(self, client):
      super(SecretmanagerV1beta1.ProjectsSecretsVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Access(self, request, global_params=None):
      r"""Accesses a SecretVersion. This call returns the secret data.

`projects/*/secrets/*/versions/latest` is an alias to the `latest`
SecretVersion.

      Args:
        request: (SecretmanagerProjectsSecretsVersionsAccessRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessSecretVersionResponse) The response message.
      """
      config = self.GetMethodConfig('Access')
      return self._RunMethod(
          config, request, global_params=global_params)

    Access.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:access',
        http_method=u'GET',
        method_id=u'secretmanager.projects.secrets.versions.access',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:access',
        request_field='',
        request_type_name=u'SecretmanagerProjectsSecretsVersionsAccessRequest',
        response_type_name=u'AccessSecretVersionResponse',
        supports_download=False,
    )

    def Destroy(self, request, global_params=None):
      r"""Destroys a SecretVersion.

Sets the state of the SecretVersion to
DESTROYED and irrevocably destroys the
secret data.

      Args:
        request: (SecretmanagerProjectsSecretsVersionsDestroyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SecretVersion) The response message.
      """
      config = self.GetMethodConfig('Destroy')
      return self._RunMethod(
          config, request, global_params=global_params)

    Destroy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:destroy',
        http_method=u'POST',
        method_id=u'secretmanager.projects.secrets.versions.destroy',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:destroy',
        request_field=u'destroySecretVersionRequest',
        request_type_name=u'SecretmanagerProjectsSecretsVersionsDestroyRequest',
        response_type_name=u'SecretVersion',
        supports_download=False,
    )

    def Disable(self, request, global_params=None):
      r"""Disables a SecretVersion.

Sets the state of the SecretVersion to
DISABLED.

      Args:
        request: (SecretmanagerProjectsSecretsVersionsDisableRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SecretVersion) The response message.
      """
      config = self.GetMethodConfig('Disable')
      return self._RunMethod(
          config, request, global_params=global_params)

    Disable.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:disable',
        http_method=u'POST',
        method_id=u'secretmanager.projects.secrets.versions.disable',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:disable',
        request_field=u'disableSecretVersionRequest',
        request_type_name=u'SecretmanagerProjectsSecretsVersionsDisableRequest',
        response_type_name=u'SecretVersion',
        supports_download=False,
    )

    def Enable(self, request, global_params=None):
      r"""Enables a SecretVersion.

Sets the state of the SecretVersion to
ENABLED.

      Args:
        request: (SecretmanagerProjectsSecretsVersionsEnableRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SecretVersion) The response message.
      """
      config = self.GetMethodConfig('Enable')
      return self._RunMethod(
          config, request, global_params=global_params)

    Enable.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:enable',
        http_method=u'POST',
        method_id=u'secretmanager.projects.secrets.versions.enable',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:enable',
        request_field=u'enableSecretVersionRequest',
        request_type_name=u'SecretmanagerProjectsSecretsVersionsEnableRequest',
        response_type_name=u'SecretVersion',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets metadata for a SecretVersion.

`projects/*/secrets/*/versions/latest` is an alias to the `latest`
SecretVersion.

      Args:
        request: (SecretmanagerProjectsSecretsVersionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SecretVersion) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}',
        http_method=u'GET',
        method_id=u'secretmanager.projects.secrets.versions.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'SecretmanagerProjectsSecretsVersionsGetRequest',
        response_type_name=u'SecretVersion',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists SecretVersions. This call does not return secret.
data.

      Args:
        request: (SecretmanagerProjectsSecretsVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSecretVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}/versions',
        http_method=u'GET',
        method_id=u'secretmanager.projects.secrets.versions.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/versions',
        request_field='',
        request_type_name=u'SecretmanagerProjectsSecretsVersionsListRequest',
        response_type_name=u'ListSecretVersionsResponse',
        supports_download=False,
    )

  class ProjectsSecretsService(base_api.BaseApiService):
    """Service class for the projects_secrets resource."""

    _NAME = u'projects_secrets'

    def __init__(self, client):
      super(SecretmanagerV1beta1.ProjectsSecretsService, self).__init__(client)
      self._upload_configs = {
          }

    def AddVersion(self, request, global_params=None):
      r"""Creates a new SecretVersion containing secret data and attaches.
it to an existing Secret.

      Args:
        request: (SecretmanagerProjectsSecretsAddVersionRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SecretVersion) The response message.
      """
      config = self.GetMethodConfig('AddVersion')
      return self._RunMethod(
          config, request, global_params=global_params)

    AddVersion.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}:addVersion',
        http_method=u'POST',
        method_id=u'secretmanager.projects.secrets.addVersion',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta1/{+parent}:addVersion',
        request_field=u'addSecretVersionRequest',
        request_type_name=u'SecretmanagerProjectsSecretsAddVersionRequest',
        response_type_name=u'SecretVersion',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates a new Secret containing no SecretVersions.

      Args:
        request: (SecretmanagerProjectsSecretsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Secret) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets',
        http_method=u'POST',
        method_id=u'secretmanager.projects.secrets.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'secretId'],
        relative_path=u'v1beta1/{+parent}/secrets',
        request_field=u'secret',
        request_type_name=u'SecretmanagerProjectsSecretsCreateRequest',
        response_type_name=u'Secret',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Secret.

      Args:
        request: (SecretmanagerProjectsSecretsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}',
        http_method=u'DELETE',
        method_id=u'secretmanager.projects.secrets.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'SecretmanagerProjectsSecretsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets metadata for a given Secret.

      Args:
        request: (SecretmanagerProjectsSecretsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Secret) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}',
        http_method=u'GET',
        method_id=u'secretmanager.projects.secrets.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'SecretmanagerProjectsSecretsGetRequest',
        response_type_name=u'Secret',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a secret.
Returns empty policy if the secret exists and does not have a policy set.

      Args:
        request: (SecretmanagerProjectsSecretsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'secretmanager.projects.secrets.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[u'options_requestedPolicyVersion'],
        relative_path=u'v1beta1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'SecretmanagerProjectsSecretsGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Secrets.

      Args:
        request: (SecretmanagerProjectsSecretsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSecretsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets',
        http_method=u'GET',
        method_id=u'secretmanager.projects.secrets.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+parent}/secrets',
        request_field='',
        request_type_name=u'SecretmanagerProjectsSecretsListRequest',
        response_type_name=u'ListSecretsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates metadata of an existing Secret.

      Args:
        request: (SecretmanagerProjectsSecretsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Secret) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}',
        http_method=u'PATCH',
        method_id=u'secretmanager.projects.secrets.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1beta1/{+name}',
        request_field=u'secret',
        request_type_name=u'SecretmanagerProjectsSecretsPatchRequest',
        response_type_name=u'Secret',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified secret. Replaces any.
existing policy.

Permissions on SecretVersions are enforced according
to the policy set on the associated Secret.

      Args:
        request: (SecretmanagerProjectsSecretsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'secretmanager.projects.secrets.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'SecretmanagerProjectsSecretsSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has for the specified secret.
If the secret does not exist, this call returns an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (SecretmanagerProjectsSecretsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/secrets/{secretsId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'secretmanager.projects.secrets.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1beta1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'SecretmanagerProjectsSecretsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(SecretmanagerV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
