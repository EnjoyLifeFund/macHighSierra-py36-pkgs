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


class RestartNodeDescription(Model):
    """Describes the parameters to restart a Service Fabric node.

    :param node_instance_id: The instance id of the target node. If instance
     id is specified the node is restarted only if it matches with the
     current instance of the node. A default value of "0" would match any
     instance id. The instance id can be obtained using get node query.
     Default value: "0" .
    :type node_instance_id: str
    :param create_fabric_dump: Specify True to create a dump of the fabric
     node process. This is case sensitive. Possible values include: 'False',
     'True'. Default value: "False" .
    :type create_fabric_dump: str
    """ 

    _validation = {
        'node_instance_id': {'required': True},
    }

    _attribute_map = {
        'node_instance_id': {'key': 'NodeInstanceId', 'type': 'str'},
        'create_fabric_dump': {'key': 'CreateFabricDump', 'type': 'str'},
    }

    def __init__(self, node_instance_id="0", create_fabric_dump="False"):
        self.node_instance_id = node_instance_id
        self.create_fabric_dump = create_fabric_dump
