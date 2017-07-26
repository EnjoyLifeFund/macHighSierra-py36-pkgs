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

from msrest.serialization import Model


class PrivateAccessServicePropertiesFormat(Model):
    """The private access service properties.

    :param service: The type of the private access.
    :type service: str
    :param locations: A list of locations.
    :type locations: list of str
    :param provisioning_state: The provisioning state of the resource.
    :type provisioning_state: str
    """

    _attribute_map = {
        'service': {'key': 'service', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(self, service=None, locations=None, provisioning_state=None):
        self.service = service
        self.locations = locations
        self.provisioning_state = provisioning_state
