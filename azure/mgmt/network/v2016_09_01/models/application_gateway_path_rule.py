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


class ApplicationGatewayPathRule(SubResource):
    """Path rule of URL path map of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param paths: Path rules of URL path map.
    :type paths: list[str]
    :param backend_address_pool: Backend address pool resource of URL path
     map.
    :type backend_address_pool:
     ~azure.mgmt.network.v2016_09_01.models.SubResource
    :param backend_http_settings: Backend http settings resource of URL path
     map.
    :type backend_http_settings:
     ~azure.mgmt.network.v2016_09_01.models.SubResource
    :param provisioning_state: Path rule of URL path map resource. Possible
     values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'paths': {'key': 'properties.paths', 'type': '[str]'},
        'backend_address_pool': {'key': 'properties.backendAddressPool', 'type': 'SubResource'},
        'backend_http_settings': {'key': 'properties.backendHttpSettings', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, paths=None, backend_address_pool=None, backend_http_settings=None, provisioning_state=None, name=None, etag=None):
        super(ApplicationGatewayPathRule, self).__init__(id=id)
        self.paths = paths
        self.backend_address_pool = backend_address_pool
        self.backend_http_settings = backend_http_settings
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
