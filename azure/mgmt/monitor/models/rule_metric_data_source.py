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

from .rule_data_source import RuleDataSource


class RuleMetricDataSource(RuleDataSource):
    """A rule metric data source. The discriminator value is always
    RuleMetricDataSource in this case.

    :param resource_uri: the resource identifier of the resource the rule
     monitors.
    :type resource_uri: str
    :param odatatype: Polymorphic Discriminator
    :type odatatype: str
    :param metric_name: the name of the metric that defines what the rule
     monitors.
    :type metric_name: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'resource_uri': {'key': 'resourceUri', 'type': 'str'},
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'metric_name': {'key': 'metricName', 'type': 'str'},
    }

    def __init__(self, resource_uri=None, metric_name=None):
        super(RuleMetricDataSource, self).__init__(resource_uri=resource_uri)
        self.metric_name = metric_name
        self.odatatype = 'Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource'