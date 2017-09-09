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

from .service_update_description import ServiceUpdateDescription


class StatefulServiceUpdateDescription(ServiceUpdateDescription):
    """Describes an update for a stateful service.

    :param flags: Flags indicating whether other properties are set. Each of
     the associated properties corresponds to a flag, specified below, which,
     if set, indicate that the property is specified.
     This property can be a combination of those flags obtained using bitwise
     'OR' operator.
     For example, if the provided value is 6 then the flags for
     ReplicaRestartWaitDuration (2) and QuorumLossWaitDuration (4) are set.
     - None - Does not indicate any other properties are set. The value is
     zero.
     - TargetReplicaSetSize/InstanceCount - Indicates whether the
     TargetReplicaSetSize property (for Stateful services) or the
     InstanceCount property (for Stateless services) is set. The value is 1.
     - ReplicaRestartWaitDuration - Indicates the ReplicaRestartWaitDuration
     property is set. The value is  2.
     - QuorumLossWaitDuration - Indicates the QuorumLossWaitDuration property
     is set. The value is 4.
     - StandByReplicaKeepDuration - Indicates the StandByReplicaKeepDuration
     property is set. The value is 8.
     - MinReplicaSetSize - Indicates the MinReplicaSetSize property is set.
     The value is 16.
     - PlacementConstraints - Indicates the PlacementConstraints property is
     set. The value is 32.
     - PlacementPolicyList - Indicates the ServicePlacementPolicies property
     is set. The value is 64.
     - Correlation - Indicates the CorrelationScheme property is set. The
     value is 128.
     - Metrics - Indicates the ServiceLoadMetrics property is set. The value
     is 256.
     - DefaultMoveCost - Indicates the DefaultMoveCost property is set. The
     value is 512.
    :type flags: str
    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and
     allow for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme: The correlation scheme.
    :type correlation_scheme: list of :class:`ServiceCorrelationDescription
     <azure.servicefabric.models.ServiceCorrelationDescription>`
    :param load_metrics: The service load metrics.
    :type load_metrics: list of :class:`ServiceLoadMetricDescription
     <azure.servicefabric.models.ServiceLoadMetricDescription>`
    :param service_placement_policies: The service placement policies.
    :type service_placement_policies: list of
     :class:`ServicePlacementPolicyDescription
     <azure.servicefabric.models.ServicePlacementPolicyDescription>`
    :param default_move_cost: The move cost for the service. Possible values
     include: 'Zero', 'Low', 'Medium', 'High'
    :type default_move_cost: str
    :param ServiceKind: Polymorphic Discriminator
    :type ServiceKind: str
    :param target_replica_set_size: The target replica set size as a number.
    :type target_replica_set_size: int
    :param min_replica_set_size: The minimum replica set size as a number.
    :type min_replica_set_size: int
    :param replica_restart_wait_duration_seconds: The duration, in seconds,
     between when a replica goes down and when a new replica is created.
    :type replica_restart_wait_duration_seconds: str
    :param quorum_loss_wait_duration_seconds: The maximum duration, in
     seconds, for which a partition is allowed to be in a state of quorum
     loss.
    :type quorum_loss_wait_duration_seconds: str
    :param stand_by_replica_keep_duration_seconds: The definition on how long
     StandBy replicas should be maintained before being removed.
    :type stand_by_replica_keep_duration_seconds: str
    """ 

    _validation = {
        'ServiceKind': {'required': True},
        'target_replica_set_size': {'minimum': 1},
        'min_replica_set_size': {'minimum': 1},
    }

    _attribute_map = {
        'flags': {'key': 'Flags', 'type': 'str'},
        'placement_constraints': {'key': 'PlacementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'CorrelationScheme', 'type': '[ServiceCorrelationDescription]'},
        'load_metrics': {'key': 'LoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'ServicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'DefaultMoveCost', 'type': 'str'},
        'ServiceKind': {'key': 'ServiceKind', 'type': 'str'},
        'target_replica_set_size': {'key': 'TargetReplicaSetSize', 'type': 'int'},
        'min_replica_set_size': {'key': 'MinReplicaSetSize', 'type': 'int'},
        'replica_restart_wait_duration_seconds': {'key': 'ReplicaRestartWaitDurationSeconds', 'type': 'str'},
        'quorum_loss_wait_duration_seconds': {'key': 'QuorumLossWaitDurationSeconds', 'type': 'str'},
        'stand_by_replica_keep_duration_seconds': {'key': 'StandByReplicaKeepDurationSeconds', 'type': 'str'},
    }

    def __init__(self, flags=None, placement_constraints=None, correlation_scheme=None, load_metrics=None, service_placement_policies=None, default_move_cost=None, target_replica_set_size=None, min_replica_set_size=None, replica_restart_wait_duration_seconds=None, quorum_loss_wait_duration_seconds=None, stand_by_replica_keep_duration_seconds=None):
        super(StatefulServiceUpdateDescription, self).__init__(flags=flags, placement_constraints=placement_constraints, correlation_scheme=correlation_scheme, load_metrics=load_metrics, service_placement_policies=service_placement_policies, default_move_cost=default_move_cost)
        self.target_replica_set_size = target_replica_set_size
        self.min_replica_set_size = min_replica_set_size
        self.replica_restart_wait_duration_seconds = replica_restart_wait_duration_seconds
        self.quorum_loss_wait_duration_seconds = quorum_loss_wait_duration_seconds
        self.stand_by_replica_keep_duration_seconds = stand_by_replica_keep_duration_seconds
        self.ServiceKind = 'Stateful'
