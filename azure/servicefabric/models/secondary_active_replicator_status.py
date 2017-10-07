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

from .secondary_replicator_status import SecondaryReplicatorStatus


class SecondaryActiveReplicatorStatus(SecondaryReplicatorStatus):
    """Status of the secondary replicator when it is in active mode and is part of
    the replica set.

    :param kind: Polymorphic Discriminator
    :type kind: str
    :param replication_queue_status:
    :type replication_queue_status: :class:`ReplicatorQueueStatus
     <azure.servicefabric.models.ReplicatorQueueStatus>`
    :param last_replication_operation_received_time_utc: The last time-stamp
     (UTC) at which a replication operation was received from the primary.
     UTC 0 represents an invalid value, indicating that a replication operation
     message was never received.
    :type last_replication_operation_received_time_utc: datetime
    :param is_in_build: Value that indicates whether the replica is currently
     being built.
    :type is_in_build: bool
    :param copy_queue_status:
    :type copy_queue_status: :class:`ReplicatorQueueStatus
     <azure.servicefabric.models.ReplicatorQueueStatus>`
    :param last_copy_operation_received_time_utc: The last time-stamp (UTC) at
     which a copy operation was received from the primary.
     UTC 0 represents an invalid value, indicating that a copy operation
     message was never received.
    :type last_copy_operation_received_time_utc: datetime
    :param last_acknowledgement_sent_time_utc: The last time-stamp (UTC) at
     which an acknowledgment was sent to the primary replicator.
     UTC 0 represents an invalid value, indicating that an acknowledgment
     message was never sent.
    :type last_acknowledgement_sent_time_utc: datetime
    """

    _validation = {
        'kind': {'required': True},
    }

    def __init__(self, replication_queue_status=None, last_replication_operation_received_time_utc=None, is_in_build=None, copy_queue_status=None, last_copy_operation_received_time_utc=None, last_acknowledgement_sent_time_utc=None):
        super(SecondaryActiveReplicatorStatus, self).__init__(replication_queue_status=replication_queue_status, last_replication_operation_received_time_utc=last_replication_operation_received_time_utc, is_in_build=is_in_build, copy_queue_status=copy_queue_status, last_copy_operation_received_time_utc=last_copy_operation_received_time_utc, last_acknowledgement_sent_time_utc=last_acknowledgement_sent_time_utc)
        self.kind = 'ActiveSecondary'
