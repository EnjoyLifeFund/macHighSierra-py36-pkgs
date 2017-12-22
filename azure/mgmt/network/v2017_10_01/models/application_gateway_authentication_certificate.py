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


class ApplicationGatewayAuthenticationCertificate(SubResource):
    """Authentication certificates of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param data: Certificate public data.
    :type data: str
    :param provisioning_state: Provisioning state of the authentication
     certificate resource. Possible values are: 'Updating', 'Deleting', and
     'Failed'.
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
        'data': {'key': 'properties.data', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, id=None, data=None, provisioning_state=None, name=None, etag=None, type=None):
        super(ApplicationGatewayAuthenticationCertificate, self).__init__(id=id)
        self.data = data
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
        self.type = type
