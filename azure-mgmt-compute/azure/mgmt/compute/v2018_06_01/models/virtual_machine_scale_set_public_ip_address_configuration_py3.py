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


class VirtualMachineScaleSetPublicIPAddressConfiguration(Model):
    """Describes a virtual machines scale set IP Configuration's PublicIPAddress
    configuration.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The publicIP address configuration name.
    :type name: str
    :param idle_timeout_in_minutes: The idle timeout of the public IP address.
    :type idle_timeout_in_minutes: int
    :param dns_settings: The dns settings to be applied on the publicIP
     addresses .
    :type dns_settings:
     ~azure.mgmt.compute.v2018_06_01.models.VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
    :param ip_tags: The list of IP tags associated with the public IP address.
    :type ip_tags:
     list[~azure.mgmt.compute.v2018_06_01.models.VirtualMachineScaleSetIpTag]
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'dns_settings': {'key': 'properties.dnsSettings', 'type': 'VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings'},
        'ip_tags': {'key': 'properties.ipTags', 'type': '[VirtualMachineScaleSetIpTag]'},
    }

    def __init__(self, *, name: str, idle_timeout_in_minutes: int=None, dns_settings=None, ip_tags=None, **kwargs) -> None:
        super(VirtualMachineScaleSetPublicIPAddressConfiguration, self).__init__(**kwargs)
        self.name = name
        self.idle_timeout_in_minutes = idle_timeout_in_minutes
        self.dns_settings = dns_settings
        self.ip_tags = ip_tags