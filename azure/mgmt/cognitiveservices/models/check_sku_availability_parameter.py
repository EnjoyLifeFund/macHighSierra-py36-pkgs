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


class CheckSkuAvailabilityParameter(Model):
    """Check SKU availability parameter.

    :param skus: The SKU of the resource.
    :type skus: list of :class:`Sku <azure.mgmt.cognitiveservices.models.Sku>`
    :param kind: The Kind of the resource. Possible values include:
     'Academic', 'Bing.Autosuggest', 'Bing.Search', 'Bing.Speech',
     'Bing.SpellCheck', 'ComputerVision', 'ContentModerator', 'CustomSpeech',
     'Emotion', 'Face', 'LUIS', 'Recommendations', 'SpeakerRecognition',
     'Speech', 'SpeechTranslation', 'TextAnalytics', 'TextTranslation', 'WebLM'
    :type kind: str or :class:`Kind
     <azure.mgmt.cognitiveservices.models.Kind>`
    :param type: The Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'skus': {'key': 'skus', 'type': '[Sku]'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, skus=None, kind=None, type=None):
        self.skus = skus
        self.kind = kind
        self.type = type
