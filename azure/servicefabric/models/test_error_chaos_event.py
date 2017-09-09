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

from .chaos_event import ChaosEvent


class TestErrorChaosEvent(ChaosEvent):
    """Describes a Chaos event that gets generated when an unexpected event
    occurs in the Chaos engine.
    For example, due to the cluster snapshot being inconsistent, while
    faulting a faultable entity, Chaos found that the entity was alreay
    faulted -- which would be an unexpected event.
    .

    :param time_stamp_utc:
    :type time_stamp_utc: datetime
    :param Kind: Polymorphic Discriminator
    :type Kind: str
    :param reason:
    :type reason: str
    """ 

    _validation = {
        'time_stamp_utc': {'required': True},
        'Kind': {'required': True},
    }

    _attribute_map = {
        'time_stamp_utc': {'key': 'TimeStampUtc', 'type': 'iso-8601'},
        'Kind': {'key': 'Kind', 'type': 'str'},
        'reason': {'key': 'Reason', 'type': 'str'},
    }

    def __init__(self, time_stamp_utc, reason=None):
        super(TestErrorChaosEvent, self).__init__(time_stamp_utc=time_stamp_utc)
        self.reason = reason
        self.Kind = 'TestError'
