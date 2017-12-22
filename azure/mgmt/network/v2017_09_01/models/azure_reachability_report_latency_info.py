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


class AzureReachabilityReportLatencyInfo(Model):
    """Details on latency for a time series.

    :param time_stamp: The time stamp.
    :type time_stamp: datetime
    :param score: The relative latency score between 1 and 100, higher values
     indicating a faster connection.
    :type score: int
    """

    _validation = {
        'score': {'maximum': 100, 'minimum': 1},
    }

    _attribute_map = {
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'score': {'key': 'score', 'type': 'int'},
    }

    def __init__(self, time_stamp=None, score=None):
        self.time_stamp = time_stamp
        self.score = score
