"""Generated client library for secretmanager version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.secretmanager.v1 import secretmanager_v1_messages as messages


class SecretmanagerV1(base_api.BaseApiClient):
  """Generated client library for service secretmanager version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://secretmanager.googleapis.com/'
  MTLS_BASE_URL = 'https://secretmanager.mtls.googleapis.com/'

  _PACKAGE = 'secretmanager'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'SecretmanagerV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new secretmanager handle."""
    url = url or self.BASE_URL
    super(SecretmanagerV1, self).__init__(
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

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(SecretmanagerV1.ProjectsLocationsService, self).__init__(client)
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
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='secretmanager.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='SecretmanagerProjectsLocationsGetRequest',
        response_type_name='Location',
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
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='secretmanager.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='SecretmanagerProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsSecretsVersionsService(base_api.BaseApiService):
    """Service class for the projects_secrets_versions resource."""

    _NAME = 'projects_secrets_versions'

    def __init__(self, client):
      super(SecretmanagerV1.ProjectsSecretsVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Access(self, request, global_params=None):
      r"""Accesses a SecretVersion. This call returns the secret data. `projects/*/secrets/*/versions/latest` is an alias to the `latest` SecretVersion.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:access',
        http_method='GET',
        method_id='secretmanager.projects.secrets.versions.access',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:access',
        request_field='',
        request_type_name='SecretmanagerProjectsSecretsVersionsAccessRequest',
        response_type_name='AccessSecretVersionResponse',
        supports_download=False,
    )

    def Destroy(self, request, global_params=None):
      r"""Destroys a SecretVersion. Sets the state of the SecretVersion to DESTROYED and irrevocably destroys the secret data.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:destroy',
        http_method='POST',
        method_id='secretmanager.projects.secrets.versions.destroy',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:destroy',
        request_field='destroySecretVersionRequest',
        request_type_name='SecretmanagerProjectsSecretsVersionsDestroyRequest',
        response_type_name='SecretVersion',
        supports_download=False,
    )

    def Disable(self, request, global_params=None):
      r"""Disables a SecretVersion. Sets the state of the SecretVersion to DISABLED.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:disable',
        http_method='POST',
        method_id='secretmanager.projects.secrets.versions.disable',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:disable',
        request_field='disableSecretVersionRequest',
        request_type_name='SecretmanagerProjectsSecretsVersionsDisableRequest',
        response_type_name='SecretVersion',
        supports_download=False,
    )

    def Enable(self, request, global_params=None):
      r"""Enables a SecretVersion. Sets the state of the SecretVersion to ENABLED.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}:enable',
        http_method='POST',
        method_id='secretmanager.projects.secrets.versions.enable',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:enable',
        request_field='enableSecretVersionRequest',
        request_type_name='SecretmanagerProjectsSecretsVersionsEnableRequest',
        response_type_name='SecretVersion',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets metadata for a SecretVersion. `projects/*/secrets/*/versions/latest` is an alias to the `latest` SecretVersion.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}/versions/{versionsId}',
        http_method='GET',
        method_id='secretmanager.projects.secrets.versions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='SecretmanagerProjectsSecretsVersionsGetRequest',
        response_type_name='SecretVersion',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists SecretVersions. This call does not return secret data.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}/versions',
        http_method='GET',
        method_id='secretmanager.projects.secrets.versions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/versions',
        request_field='',
        request_type_name='SecretmanagerProjectsSecretsVersionsListRequest',
        response_type_name='ListSecretVersionsResponse',
        supports_download=False,
    )

  class ProjectsSecretsService(base_api.BaseApiService):
    """Service class for the projects_secrets resource."""

    _NAME = 'projects_secrets'

    def __init__(self, client):
      super(SecretmanagerV1.ProjectsSecretsService, self).__init__(client)
      self._upload_configs = {
          }

    def AddVersion(self, request, global_params=None):
      r"""Creates a new SecretVersion containing secret data and attaches it to an existing Secret.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}:addVersion',
        http_method='POST',
        method_id='secretmanager.projects.secrets.addVersion',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}:addVersion',
        request_field='addSecretVersionRequest',
        request_type_name='SecretmanagerProjectsSecretsAddVersionRequest',
        response_type_name='SecretVersion',
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
        flat_path='v1/projects/{projectsId}/secrets',
        http_method='POST',
        method_id='secretmanager.projects.secrets.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['secretId'],
        relative_path='v1/{+parent}/secrets',
        request_field='secret',
        request_type_name='SecretmanagerProjectsSecretsCreateRequest',
        response_type_name='Secret',
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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}',
        http_method='DELETE',
        method_id='secretmanager.projects.secrets.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='SecretmanagerProjectsSecretsDeleteRequest',
        response_type_name='Empty',
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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}',
        http_method='GET',
        method_id='secretmanager.projects.secrets.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='SecretmanagerProjectsSecretsGetRequest',
        response_type_name='Secret',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a secret. Returns empty policy if the secret exists and does not have a policy set.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}:getIamPolicy',
        http_method='GET',
        method_id='secretmanager.projects.secrets.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='SecretmanagerProjectsSecretsGetIamPolicyRequest',
        response_type_name='Policy',
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
        flat_path='v1/projects/{projectsId}/secrets',
        http_method='GET',
        method_id='secretmanager.projects.secrets.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/secrets',
        request_field='',
        request_type_name='SecretmanagerProjectsSecretsListRequest',
        response_type_name='ListSecretsResponse',
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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}',
        http_method='PATCH',
        method_id='secretmanager.projects.secrets.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='secret',
        request_type_name='SecretmanagerProjectsSecretsPatchRequest',
        response_type_name='Secret',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified secret. Replaces any existing policy. Permissions on SecretVersions are enforced according to the policy set on the associated Secret.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}:setIamPolicy',
        http_method='POST',
        method_id='secretmanager.projects.secrets.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='SecretmanagerProjectsSecretsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has for the specified secret. If the secret does not exist, this call returns an empty set of permissions, not a NOT_FOUND error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

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
        flat_path='v1/projects/{projectsId}/secrets/{secretsId}:testIamPermissions',
        http_method='POST',
        method_id='secretmanager.projects.secrets.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='SecretmanagerProjectsSecretsTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(SecretmanagerV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
