# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class ApplicationGatewayUrlPathMap(SubResource):
    """UrlPathMaps give a url path to the backend mapping information for
    PathBasedRouting.

    :param id: Resource ID.
    :type id: str
    :param default_backend_address_pool: Default backend address pool resource
     of URL path map.
    :type default_backend_address_pool:
     ~azure.mgmt.network.v2017_08_01.models.SubResource
    :param default_backend_http_settings: Default backend http settings
     resource of URL path map.
    :type default_backend_http_settings:
     ~azure.mgmt.network.v2017_08_01.models.SubResource
    :param default_redirect_configuration: Default redirect configuration
     resource of URL path map.
    :type default_redirect_configuration:
     ~azure.mgmt.network.v2017_08_01.models.SubResource
    :param path_rules: Path rule of URL path map resource.
    :type path_rules:
     list[~azure.mgmt.network.v2017_08_01.models.ApplicationGatewayPathRule]
    :param provisioning_state: Provisioning state of the backend http settings
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'default_backend_address_pool': {'key': 'properties.defaultBackendAddressPool', 'type': 'SubResource'},
        'default_backend_http_settings': {'key': 'properties.defaultBackendHttpSettings', 'type': 'SubResource'},
        'default_redirect_configuration': {'key': 'properties.defaultRedirectConfiguration', 'type': 'SubResource'},
        'path_rules': {'key': 'properties.pathRules', 'type': '[ApplicationGatewayPathRule]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, id=None, default_backend_address_pool=None, default_backend_http_settings=None, default_redirect_configuration=None, path_rules=None, provisioning_state=None, name=None, etag=None, type=None):
        super(ApplicationGatewayUrlPathMap, self).__init__(id=id)
        self.default_backend_address_pool = default_backend_address_pool
        self.default_backend_http_settings = default_backend_http_settings
        self.default_redirect_configuration = default_redirect_configuration
        self.path_rules = path_rules
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
        self.type = type
