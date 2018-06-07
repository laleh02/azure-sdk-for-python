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

from .integration_runtime_py3 import IntegrationRuntime


class SelfHostedIntegrationRuntime(IntegrationRuntime):
    """Self-hosted integration runtime.

    All required parameters must be populated in order to send to Azure.

    :param description: Integration runtime description.
    :type description: str
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_info:
    :type linked_info:
     ~azure.mgmt.datafactory.models.LinkedIntegrationRuntimeProperties
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_info': {'key': 'typeProperties.linkedInfo', 'type': 'LinkedIntegrationRuntimeProperties'},
    }

    def __init__(self, *, description: str=None, linked_info=None, **kwargs) -> None:
        super(SelfHostedIntegrationRuntime, self).__init__(description=description, **kwargs)
        self.linked_info = linked_info
        self.type = 'SelfHosted'