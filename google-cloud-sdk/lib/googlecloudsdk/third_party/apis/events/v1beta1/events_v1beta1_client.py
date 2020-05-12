"""Generated client library for events version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.events.v1beta1 import events_v1beta1_messages as messages


class EventsV1beta1(base_api.BaseApiClient):
  """Generated client library for service events version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://events.googleapis.com/'
  MTLS_BASE_URL = u'https://events.mtls.googleapis.com/'

  _PACKAGE = u'events'
  _SCOPES = ['https://www.googleapis.com/auth/userinfo.email']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = u'google-cloud-sdk'
  _CLIENT_CLASS_NAME = u'EventsV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new events handle."""
    url = url or self.BASE_URL
    super(EventsV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.customresourcedefinitions = self.CustomresourcedefinitionsService(self)
    self.namespaces_customresourcedefinitions = self.NamespacesCustomresourcedefinitionsService(self)
    self.namespaces_triggers = self.NamespacesTriggersService(self)
    self.namespaces = self.NamespacesService(self)
    self.projects_locations_customresourcedefinitions = self.ProjectsLocationsCustomresourcedefinitionsService(self)
    self.projects_locations_triggers = self.ProjectsLocationsTriggersService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class CustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the customresourcedefinitions resource."""

    _NAME = u'customresourcedefinitions'

    def __init__(self, client):
      super(EventsV1beta1.CustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Rpc to list custom resource definitions.

      Args:
        request: (EventsCustomresourcedefinitionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCustomResourceDefinitionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'events.customresourcedefinitions.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'continue_', u'fieldSelector', u'includeUninitialized', u'labelSelector', u'limit', u'parent', u'resourceVersion', u'watch'],
        relative_path=u'apis/apiextensions.k8s.io/v1beta1/customresourcedefinitions',
        request_field='',
        request_type_name=u'EventsCustomresourcedefinitionsListRequest',
        response_type_name=u'ListCustomResourceDefinitionsResponse',
        supports_download=False,
    )

  class NamespacesCustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the namespaces_customresourcedefinitions resource."""

    _NAME = u'namespaces_customresourcedefinitions'

    def __init__(self, client):
      super(EventsV1beta1.NamespacesCustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a CustomResourceDefinition.

      Args:
        request: (EventsNamespacesCustomresourcedefinitionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomResourceDefinition) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'apis/apiextensions.k8s.io/v1beta1/namespaces/{namespacesId}/customresourcedefinitions/{customresourcedefinitionsId}',
        http_method=u'GET',
        method_id=u'events.namespaces.customresourcedefinitions.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'apis/apiextensions.k8s.io/v1beta1/{+name}',
        request_field='',
        request_type_name=u'EventsNamespacesCustomresourcedefinitionsGetRequest',
        response_type_name=u'CustomResourceDefinition',
        supports_download=False,
    )

  class NamespacesTriggersService(base_api.BaseApiService):
    """Service class for the namespaces_triggers resource."""

    _NAME = u'namespaces_triggers'

    def __init__(self, client):
      super(EventsV1beta1.NamespacesTriggersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new trigger.

      Args:
        request: (EventsNamespacesTriggersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers',
        http_method=u'POST',
        method_id=u'events.namespaces.triggers.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'apis/eventing.knative.dev/v1beta1/{+parent}/triggers',
        request_field=u'trigger',
        request_type_name=u'EventsNamespacesTriggersCreateRequest',
        response_type_name=u'Trigger',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Rpc to delete a trigger.

      Args:
        request: (EventsNamespacesTriggersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers/{triggersId}',
        http_method=u'DELETE',
        method_id=u'events.namespaces.triggers.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'apiVersion', u'kind', u'propagationPolicy'],
        relative_path=u'apis/eventing.knative.dev/v1beta1/{+name}',
        request_field='',
        request_type_name=u'EventsNamespacesTriggersDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a trigger.

      Args:
        request: (EventsNamespacesTriggersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers/{triggersId}',
        http_method=u'GET',
        method_id=u'events.namespaces.triggers.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'apis/eventing.knative.dev/v1beta1/{+name}',
        request_field='',
        request_type_name=u'EventsNamespacesTriggersGetRequest',
        response_type_name=u'Trigger',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list triggers.

      Args:
        request: (EventsNamespacesTriggersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTriggersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers',
        http_method=u'GET',
        method_id=u'events.namespaces.triggers.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'continue_', u'fieldSelector', u'includeUninitialized', u'labelSelector', u'limit', u'resourceVersion', u'watch'],
        relative_path=u'apis/eventing.knative.dev/v1beta1/{+parent}/triggers',
        request_field='',
        request_type_name=u'EventsNamespacesTriggersListRequest',
        response_type_name=u'ListTriggersResponse',
        supports_download=False,
    )

    def ReplaceTrigger(self, request, global_params=None):
      r"""Rpc to replace a trigger.

Only the spec and metadata labels and annotations are modifiable. After
the Update request, Events for Cloud Run will work to make the 'status'
match the requested 'spec'.

May provide metadata.resourceVersion to enforce update from last read for
optimistic concurrency control.

      Args:
        request: (EventsNamespacesTriggersReplaceTriggerRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('ReplaceTrigger')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceTrigger.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'apis/eventing.knative.dev/v1beta1/namespaces/{namespacesId}/triggers/{triggersId}',
        http_method=u'PUT',
        method_id=u'events.namespaces.triggers.replaceTrigger',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'apis/eventing.knative.dev/v1beta1/{+name}',
        request_field=u'trigger',
        request_type_name=u'EventsNamespacesTriggersReplaceTriggerRequest',
        response_type_name=u'Trigger',
        supports_download=False,
    )

  class NamespacesService(base_api.BaseApiService):
    """Service class for the namespaces resource."""

    _NAME = u'namespaces'

    def __init__(self, client):
      super(EventsV1beta1.NamespacesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsCustomresourcedefinitionsService(base_api.BaseApiService):
    """Service class for the projects_locations_customresourcedefinitions resource."""

    _NAME = u'projects_locations_customresourcedefinitions'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsLocationsCustomresourcedefinitionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a CustomResourceDefinition.

      Args:
        request: (EventsProjectsLocationsCustomresourcedefinitionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomResourceDefinition) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/customresourcedefinitions/{customresourcedefinitionsId}',
        http_method=u'GET',
        method_id=u'events.projects.locations.customresourcedefinitions.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'EventsProjectsLocationsCustomresourcedefinitionsGetRequest',
        response_type_name=u'CustomResourceDefinition',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list custom resource definitions.

      Args:
        request: (EventsProjectsLocationsCustomresourcedefinitionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCustomResourceDefinitionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/customresourcedefinitions',
        http_method=u'GET',
        method_id=u'events.projects.locations.customresourcedefinitions.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'continue_', u'fieldSelector', u'includeUninitialized', u'labelSelector', u'limit', u'resourceVersion', u'watch'],
        relative_path=u'v1beta1/{+parent}/customresourcedefinitions',
        request_field='',
        request_type_name=u'EventsProjectsLocationsCustomresourcedefinitionsListRequest',
        response_type_name=u'ListCustomResourceDefinitionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsTriggersService(base_api.BaseApiService):
    """Service class for the projects_locations_triggers resource."""

    _NAME = u'projects_locations_triggers'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsLocationsTriggersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new trigger.

      Args:
        request: (EventsProjectsLocationsTriggersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/triggers',
        http_method=u'POST',
        method_id=u'events.projects.locations.triggers.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta1/{+parent}/triggers',
        request_field=u'trigger',
        request_type_name=u'EventsProjectsLocationsTriggersCreateRequest',
        response_type_name=u'Trigger',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Rpc to delete a trigger.

      Args:
        request: (EventsProjectsLocationsTriggersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method=u'DELETE',
        method_id=u'events.projects.locations.triggers.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'apiVersion', u'kind', u'propagationPolicy'],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'EventsProjectsLocationsTriggersDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Rpc to get information about a trigger.

      Args:
        request: (EventsProjectsLocationsTriggersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method=u'GET',
        method_id=u'events.projects.locations.triggers.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'EventsProjectsLocationsTriggersGetRequest',
        response_type_name=u'Trigger',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Rpc to list triggers.

      Args:
        request: (EventsProjectsLocationsTriggersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTriggersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/triggers',
        http_method=u'GET',
        method_id=u'events.projects.locations.triggers.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'continue_', u'fieldSelector', u'includeUninitialized', u'labelSelector', u'limit', u'resourceVersion', u'watch'],
        relative_path=u'v1beta1/{+parent}/triggers',
        request_field='',
        request_type_name=u'EventsProjectsLocationsTriggersListRequest',
        response_type_name=u'ListTriggersResponse',
        supports_download=False,
    )

    def ReplaceTrigger(self, request, global_params=None):
      r"""Rpc to replace a trigger.

Only the spec and metadata labels and annotations are modifiable. After
the Update request, Events for Cloud Run will work to make the 'status'
match the requested 'spec'.

May provide metadata.resourceVersion to enforce update from last read for
optimistic concurrency control.

      Args:
        request: (EventsProjectsLocationsTriggersReplaceTriggerRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Trigger) The response message.
      """
      config = self.GetMethodConfig('ReplaceTrigger')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceTrigger.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/triggers/{triggersId}',
        http_method=u'PUT',
        method_id=u'events.projects.locations.triggers.replaceTrigger',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field=u'trigger',
        request_type_name=u'EventsProjectsLocationsTriggersReplaceTriggerRequest',
        response_type_name=u'Trigger',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(EventsV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
