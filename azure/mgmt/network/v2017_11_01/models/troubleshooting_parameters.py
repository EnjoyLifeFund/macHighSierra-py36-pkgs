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


class TroubleshootingParameters(Model):
    """Parameters that define the resource to troubleshoot.

    :param target_resource_id: The target resource to troubleshoot.
    :type target_resource_id: str
    :param storage_id: The ID for the storage account to save the troubleshoot
     result.
    :type storage_id: str
    :param storage_path: The path to the blob to save the troubleshoot result
     in.
    :type storage_path: str
    """

    _validation = {
        'target_resource_id': {'required': True},
        'storage_id': {'required': True},
        'storage_path': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'storage_id': {'key': 'properties.storageId', 'type': 'str'},
        'storage_path': {'key': 'properties.storagePath', 'type': 'str'},
    }

    def __init__(self, target_resource_id, storage_id, storage_path):
        self.target_resource_id = target_resource_id
        self.storage_id = storage_id
        self.storage_path = storage_path
