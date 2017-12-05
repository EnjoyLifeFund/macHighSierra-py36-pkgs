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


class Dimension(Model):
    """Dimension of the metric.

    :param name: The name of the dimension.
    :type name: str
    :param display_name: The display name of the dimension.
    :type display_name: str
    :param internal_name: The internal name of the dimension.
    :type internal_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'internal_name': {'key': 'internalName', 'type': 'str'},
    }

    def __init__(self, name=None, display_name=None, internal_name=None):
        self.name = name
        self.display_name = display_name
        self.internal_name = internal_name
