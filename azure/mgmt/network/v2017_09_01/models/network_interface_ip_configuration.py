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


class NetworkInterfaceIPConfiguration(SubResource):
    """IPConfiguration in a network interface.

    :param id: Resource ID.
    :type id: str
    :param application_gateway_backend_address_pools: The reference of
     ApplicationGatewayBackendAddressPool resource.
    :type application_gateway_backend_address_pools:
     list[~azure.mgmt.network.v2017_09_01.models.ApplicationGatewayBackendAddressPool]
    :param load_balancer_backend_address_pools: The reference of
     LoadBalancerBackendAddressPool resource.
    :type load_balancer_backend_address_pools:
     list[~azure.mgmt.network.v2017_09_01.models.BackendAddressPool]
    :param load_balancer_inbound_nat_rules: A list of references of
     LoadBalancerInboundNatRules.
    :type load_balancer_inbound_nat_rules:
     list[~azure.mgmt.network.v2017_09_01.models.InboundNatRule]
    :param private_ip_address: Private IP address of the IP configuration.
    :type private_ip_address: str
    :param private_ip_allocation_method: Defines how a private IP address is
     assigned. Possible values are: 'Static' and 'Dynamic'. Possible values
     include: 'Static', 'Dynamic'
    :type private_ip_allocation_method: str or
     ~azure.mgmt.network.v2017_09_01.models.IPAllocationMethod
    :param private_ip_address_version: Available from Api-Version 2016-03-30
     onwards, it represents whether the specific ipconfiguration is IPv4 or
     IPv6. Default is taken as IPv4.  Possible values are: 'IPv4' and 'IPv6'.
     Possible values include: 'IPv4', 'IPv6'
    :type private_ip_address_version: str or
     ~azure.mgmt.network.v2017_09_01.models.IPVersion
    :param subnet: Subnet bound to the IP configuration.
    :type subnet: ~azure.mgmt.network.v2017_09_01.models.Subnet
    :param primary: Gets whether this is a primary customer address on the
     network interface.
    :type primary: bool
    :param public_ip_address: Public IP address bound to the IP configuration.
    :type public_ip_address:
     ~azure.mgmt.network.v2017_09_01.models.PublicIPAddress
    :param application_security_groups: Application security groups in which
     the IP configuration is included.
    :type application_security_groups:
     list[~azure.mgmt.network.v2017_09_01.models.ApplicationSecurityGroup]
    :param provisioning_state: The provisioning state of the network interface
     IP configuration. Possible values are: 'Updating', 'Deleting', and
     'Failed'.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'application_gateway_backend_address_pools': {'key': 'properties.applicationGatewayBackendAddressPools', 'type': '[ApplicationGatewayBackendAddressPool]'},
        'load_balancer_backend_address_pools': {'key': 'properties.loadBalancerBackendAddressPools', 'type': '[BackendAddressPool]'},
        'load_balancer_inbound_nat_rules': {'key': 'properties.loadBalancerInboundNatRules', 'type': '[InboundNatRule]'},
        'private_ip_address': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'private_ip_address_version': {'key': 'properties.privateIPAddressVersion', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'Subnet'},
        'primary': {'key': 'properties.primary', 'type': 'bool'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'PublicIPAddress'},
        'application_security_groups': {'key': 'properties.applicationSecurityGroups', 'type': '[ApplicationSecurityGroup]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, application_gateway_backend_address_pools=None, load_balancer_backend_address_pools=None, load_balancer_inbound_nat_rules=None, private_ip_address=None, private_ip_allocation_method=None, private_ip_address_version=None, subnet=None, primary=None, public_ip_address=None, application_security_groups=None, provisioning_state=None, name=None, etag=None):
        super(NetworkInterfaceIPConfiguration, self).__init__(id=id)
        self.application_gateway_backend_address_pools = application_gateway_backend_address_pools
        self.load_balancer_backend_address_pools = load_balancer_backend_address_pools
        self.load_balancer_inbound_nat_rules = load_balancer_inbound_nat_rules
        self.private_ip_address = private_ip_address
        self.private_ip_allocation_method = private_ip_allocation_method
        self.private_ip_address_version = private_ip_address_version
        self.subnet = subnet
        self.primary = primary
        self.public_ip_address = public_ip_address
        self.application_security_groups = application_security_groups
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag