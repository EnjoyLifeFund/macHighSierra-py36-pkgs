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


class RollingUpgradeProgressInfo(Model):
    """Information about the number of virtual machine instances in each upgrade
    state.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar successful_instance_count: The number of instances that have been
     successfully upgraded.
    :vartype successful_instance_count: int
    :ivar failed_instance_count: The number of instances that have failed to
     be upgraded successfully.
    :vartype failed_instance_count: int
    :ivar in_progress_instance_count: The number of instances that are
     currently being upgraded.
    :vartype in_progress_instance_count: int
    :ivar pending_instance_count: The number of instances that have not yet
     begun to be upgraded.
    :vartype pending_instance_count: int
    """

    _validation = {
        'successful_instance_count': {'readonly': True},
        'failed_instance_count': {'readonly': True},
        'in_progress_instance_count': {'readonly': True},
        'pending_instance_count': {'readonly': True},
    }

    _attribute_map = {
        'successful_instance_count': {'key': 'successfulInstanceCount', 'type': 'int'},
        'failed_instance_count': {'key': 'failedInstanceCount', 'type': 'int'},
        'in_progress_instance_count': {'key': 'inProgressInstanceCount', 'type': 'int'},
        'pending_instance_count': {'key': 'pendingInstanceCount', 'type': 'int'},
    }

    def __init__(self):
        self.successful_instance_count = None
        self.failed_instance_count = None
        self.in_progress_instance_count = None
        self.pending_instance_count = None
