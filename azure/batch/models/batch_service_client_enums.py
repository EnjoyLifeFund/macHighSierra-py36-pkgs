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

from enum import Enum


class OSType(Enum):

    linux = "linux"
    windows = "windows"


class AccessScope(Enum):

    job = "job"


class CertificateState(Enum):

    active = "active"
    deleting = "deleting"
    delete_failed = "deleteFailed"


class CertificateFormat(Enum):

    pfx = "pfx"
    cer = "cer"


class JobAction(Enum):

    none = "none"
    disable = "disable"
    terminate = "terminate"


class DependencyAction(Enum):

    satisfy = "satisfy"
    block = "block"


class AutoUserScope(Enum):

    task = "task"
    pool = "pool"


class ElevationLevel(Enum):

    non_admin = "nonAdmin"
    admin = "admin"


class OutputFileUploadCondition(Enum):

    task_success = "taskSuccess"
    task_failure = "taskFailure"
    task_completion = "taskCompletion"


class ComputeNodeFillType(Enum):

    spread = "spread"
    pack = "pack"


class CertificateStoreLocation(Enum):

    current_user = "currentUser"
    local_machine = "localMachine"


class CertificateVisibility(Enum):

    start_task = "startTask"
    task = "task"
    remote_user = "remoteUser"


class CachingType(Enum):

    none = "none"
    read_only = "readOnly"
    read_write = "readWrite"


class StorageAccountType(Enum):

    standard_lrs = "Standard_LRS"
    premium_lrs = "Premium_LRS"


class InboundEndpointProtocol(Enum):

    tcp = "tcp"
    udp = "udp"


class NetworkSecurityGroupRuleAccess(Enum):

    allow = "allow"
    deny = "deny"


class PoolLifetimeOption(Enum):

    job_schedule = "jobSchedule"
    job = "job"


class OnAllTasksComplete(Enum):

    no_action = "noAction"
    terminate_job = "terminateJob"


class OnTaskFailure(Enum):

    no_action = "noAction"
    perform_exit_options_job_action = "performExitOptionsJobAction"


class JobScheduleState(Enum):

    active = "active"
    completed = "completed"
    disabled = "disabled"
    terminating = "terminating"
    deleting = "deleting"


class ErrorCategory(Enum):

    user_error = "userError"
    server_error = "serverError"


class JobState(Enum):

    active = "active"
    disabling = "disabling"
    disabled = "disabled"
    enabling = "enabling"
    terminating = "terminating"
    completed = "completed"
    deleting = "deleting"


class JobPreparationTaskState(Enum):

    running = "running"
    completed = "completed"


class TaskExecutionResult(Enum):

    success = "success"
    failure = "failure"


class JobReleaseTaskState(Enum):

    running = "running"
    completed = "completed"


class TaskCountValidationStatus(Enum):

    validated = "validated"
    unvalidated = "unvalidated"


class PoolState(Enum):

    active = "active"
    deleting = "deleting"
    upgrading = "upgrading"


class AllocationState(Enum):

    steady = "steady"
    resizing = "resizing"
    stopping = "stopping"


class TaskState(Enum):

    active = "active"
    preparing = "preparing"
    running = "running"
    completed = "completed"


class TaskAddStatus(Enum):

    success = "success"
    client_error = "clientError"
    server_error = "serverError"


class SubtaskState(Enum):

    preparing = "preparing"
    running = "running"
    completed = "completed"


class StartTaskState(Enum):

    running = "running"
    completed = "completed"


class ComputeNodeState(Enum):

    idle = "idle"
    rebooting = "rebooting"
    reimaging = "reimaging"
    running = "running"
    unusable = "unusable"
    creating = "creating"
    starting = "starting"
    waiting_for_start_task = "waitingForStartTask"
    start_task_failed = "startTaskFailed"
    unknown = "unknown"
    leaving_pool = "leavingPool"
    offline = "offline"
    preempted = "preempted"


class SchedulingState(Enum):

    enabled = "enabled"
    disabled = "disabled"


class DisableJobOption(Enum):

    requeue = "requeue"
    terminate = "terminate"
    wait = "wait"


class ComputeNodeDeallocationOption(Enum):

    requeue = "requeue"
    terminate = "terminate"
    task_completion = "taskCompletion"
    retained_data = "retainedData"


class ComputeNodeRebootOption(Enum):

    requeue = "requeue"
    terminate = "terminate"
    task_completion = "taskCompletion"
    retained_data = "retainedData"


class ComputeNodeReimageOption(Enum):

    requeue = "requeue"
    terminate = "terminate"
    task_completion = "taskCompletion"
    retained_data = "retainedData"


class DisableComputeNodeSchedulingOption(Enum):

    requeue = "requeue"
    terminate = "terminate"
    task_completion = "taskCompletion"
