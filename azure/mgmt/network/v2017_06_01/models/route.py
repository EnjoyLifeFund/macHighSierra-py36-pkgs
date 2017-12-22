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


class Route(SubResource):
    """Route resource.

    :param id: Resource ID.
    :type id: str
    :param address_prefix: The destination CIDR to which the route applies.
    :type address_prefix: str
    :param next_hop_type: The type of Azure hop the packet should be sent to.
     Possible values are: 'VirtualNetworkGateway', 'VnetLocal', 'Internet',
     'VirtualAppliance', and 'None'. Possible values include:
     'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'VirtualAppliance',
     'None'
    :type next_hop_type: str or
     ~azure.mgmt.network.v2017_06_01.models.RouteNextHopType
    :param next_hop_ip_address: The IP address packets should be forwarded to.
     Next hop values are only allowed in routes where the next hop type is
     VirtualAppliance.
    :type next_hop_ip_address: str
    :param provisioning_state: The provisioning state of the resource.
     Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'next_hop_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'next_hop_type': {'key': 'properties.nextHopType', 'type': 'str'},
        'next_hop_ip_address': {'key': 'properties.nextHopIpAddress', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, next_hop_type, id=None, address_prefix=None, next_hop_ip_address=None, provisioning_state=None, name=None, etag=None):
        super(Route, self).__init__(id=id)
        self.address_prefix = address_prefix
        self.next_hop_type = next_hop_type
        self.next_hop_ip_address = next_hop_ip_address
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
