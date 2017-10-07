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

from .generic_resource import GenericResource


class ApplicationPatchable(GenericResource):
    """Information about managed application.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: :class:`Sku
     <azure.mgmt.resource.managedapplications.models.Sku>`
    :param identity: The identity of the resource.
    :type identity: :class:`Identity
     <azure.mgmt.resource.managedapplications.models.Identity>`
    :param managed_resource_group_id: The managed resource group Id.
    :type managed_resource_group_id: str
    :param application_definition_id: The fully qualified path of managed
     application definition Id.
    :type application_definition_id: str
    :param parameters: Name and value pairs that define the managed
     application parameters. It can be a JObject or a well formed JSON string.
    :type parameters: object
    :ivar outputs: Name and value pairs that define the managed application
     outputs.
    :vartype outputs: object
    :ivar provisioning_state: The managed application provisioning state.
     Possible values include: 'Accepted', 'Running', 'Ready', 'Creating',
     'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded',
     'Updating'
    :vartype provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.resource.managedapplications.models.ProvisioningState>`
    :param ui_definition_uri: The blob URI where the UI definition file is
     located.
    :type ui_definition_uri: str
    :param plan: The plan information.
    :type plan: :class:`PlanPatchable
     <azure.mgmt.resource.managedapplications.models.PlanPatchable>`
    :param kind: The kind of the managed application. Allowed values are
     MarketPlace and ServiceCatalog.
    :type kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'outputs': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'kind': {'pattern': r'^[-\w\._,\(\)]+$'},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'application_definition_id': {'key': 'properties.applicationDefinitionId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'outputs': {'key': 'properties.outputs', 'type': 'object'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'ui_definition_uri': {'key': 'properties.uiDefinitionUri', 'type': 'str'},
        'plan': {'key': 'plan', 'type': 'PlanPatchable'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, location=None, tags=None, managed_by=None, sku=None, identity=None, managed_resource_group_id=None, application_definition_id=None, parameters=None, ui_definition_uri=None, plan=None, kind=None):
        super(ApplicationPatchable, self).__init__(location=location, tags=tags, managed_by=managed_by, sku=sku, identity=identity)
        self.managed_resource_group_id = managed_resource_group_id
        self.application_definition_id = application_definition_id
        self.parameters = parameters
        self.outputs = None
        self.provisioning_state = None
        self.ui_definition_uri = ui_definition_uri
        self.plan = plan
        self.kind = kind
