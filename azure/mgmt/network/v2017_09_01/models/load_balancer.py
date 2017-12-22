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

from .resource import Resource


class LoadBalancer(Resource):
    """LoadBalancer resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param sku: The load balancer SKU.
    :type sku: ~azure.mgmt.network.v2017_09_01.models.LoadBalancerSku
    :param frontend_ip_configurations: Object representing the frontend IPs to
     be used for the load balancer
    :type frontend_ip_configurations:
     list[~azure.mgmt.network.v2017_09_01.models.FrontendIPConfiguration]
    :param backend_address_pools: Collection of backend address pools used by
     a load balancer
    :type backend_address_pools:
     list[~azure.mgmt.network.v2017_09_01.models.BackendAddressPool]
    :param load_balancing_rules: Object collection representing the load
     balancing rules Gets the provisioning
    :type load_balancing_rules:
     list[~azure.mgmt.network.v2017_09_01.models.LoadBalancingRule]
    :param probes: Collection of probe objects used in the load balancer
    :type probes: list[~azure.mgmt.network.v2017_09_01.models.Probe]
    :param inbound_nat_rules: Collection of inbound NAT Rules used by a load
     balancer. Defining inbound NAT rules on your load balancer is mutually
     exclusive with defining an inbound NAT pool. Inbound NAT pools are
     referenced from virtual machine scale sets. NICs that are associated with
     individual virtual machines cannot reference an Inbound NAT pool. They
     have to reference individual inbound NAT rules.
    :type inbound_nat_rules:
     list[~azure.mgmt.network.v2017_09_01.models.InboundNatRule]
    :param inbound_nat_pools: Defines an external port range for inbound NAT
     to a single backend port on NICs associated with a load balancer. Inbound
     NAT rules are created automatically for each NIC associated with the Load
     Balancer using an external port from this range. Defining an Inbound NAT
     pool on your Load Balancer is mutually exclusive with defining inbound Nat
     rules. Inbound NAT pools are referenced from virtual machine scale sets.
     NICs that are associated with individual virtual machines cannot reference
     an inbound NAT pool. They have to reference individual inbound NAT rules.
    :type inbound_nat_pools:
     list[~azure.mgmt.network.v2017_09_01.models.InboundNatPool]
    :param outbound_nat_rules: The outbound NAT rules.
    :type outbound_nat_rules:
     list[~azure.mgmt.network.v2017_09_01.models.OutboundNatRule]
    :param resource_guid: The resource GUID property of the load balancer
     resource.
    :type resource_guid: str
    :param provisioning_state: Gets the provisioning state of the PublicIP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'LoadBalancerSku'},
        'frontend_ip_configurations': {'key': 'properties.frontendIPConfigurations', 'type': '[FrontendIPConfiguration]'},
        'backend_address_pools': {'key': 'properties.backendAddressPools', 'type': '[BackendAddressPool]'},
        'load_balancing_rules': {'key': 'properties.loadBalancingRules', 'type': '[LoadBalancingRule]'},
        'probes': {'key': 'properties.probes', 'type': '[Probe]'},
        'inbound_nat_rules': {'key': 'properties.inboundNatRules', 'type': '[InboundNatRule]'},
        'inbound_nat_pools': {'key': 'properties.inboundNatPools', 'type': '[InboundNatPool]'},
        'outbound_nat_rules': {'key': 'properties.outboundNatRules', 'type': '[OutboundNatRule]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, location=None, tags=None, sku=None, frontend_ip_configurations=None, backend_address_pools=None, load_balancing_rules=None, probes=None, inbound_nat_rules=None, inbound_nat_pools=None, outbound_nat_rules=None, resource_guid=None, provisioning_state=None, etag=None):
        super(LoadBalancer, self).__init__(id=id, location=location, tags=tags)
        self.sku = sku
        self.frontend_ip_configurations = frontend_ip_configurations
        self.backend_address_pools = backend_address_pools
        self.load_balancing_rules = load_balancing_rules
        self.probes = probes
        self.inbound_nat_rules = inbound_nat_rules
        self.inbound_nat_pools = inbound_nat_pools
        self.outbound_nat_rules = outbound_nat_rules
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
