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


class ChaosContext(Model):
    """Describes a map, which is a collection of (string, string) type key-value
    pairs. The map can be used to record information about
    the Chaos run. There cannot be more than 100 such pairs and each string
    (key or value) can be at most 4095 characters long.
    This map is set by the starter of the Chaos run to optionally store the
    context about the specific run.
    .

    :param map:
    :type map: object
    """

    _attribute_map = {
        'map': {'key': 'Map', 'type': 'object'},
    }

    def __init__(self, map=None):
        self.map = map
