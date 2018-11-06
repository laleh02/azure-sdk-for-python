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


class SiteConfig(Model):
    """Configuration of an App Service app.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param number_of_workers: Number of workers.
    :type number_of_workers: int
    :param default_documents: Default documents.
    :type default_documents: list[str]
    :param net_framework_version: .NET Framework version. Default value:
     "v4.6" .
    :type net_framework_version: str
    :param php_version: Version of PHP.
    :type php_version: str
    :param python_version: Version of Python.
    :type python_version: str
    :param node_version: Version of Node.js.
    :type node_version: str
    :param linux_fx_version: Linux App Framework and version
    :type linux_fx_version: str
    :param windows_fx_version: Xenon App Framework and version
    :type windows_fx_version: str
    :param request_tracing_enabled: <code>true</code> if request tracing is
     enabled; otherwise, <code>false</code>.
    :type request_tracing_enabled: bool
    :param request_tracing_expiration_time: Request tracing expiration time.
    :type request_tracing_expiration_time: datetime
    :param remote_debugging_enabled: <code>true</code> if remote debugging is
     enabled; otherwise, <code>false</code>.
    :type remote_debugging_enabled: bool
    :param remote_debugging_version: Remote debugging version.
    :type remote_debugging_version: str
    :param http_logging_enabled: <code>true</code> if HTTP logging is enabled;
     otherwise, <code>false</code>.
    :type http_logging_enabled: bool
    :param logs_directory_size_limit: HTTP logs directory size limit.
    :type logs_directory_size_limit: int
    :param detailed_error_logging_enabled: <code>true</code> if detailed error
     logging is enabled; otherwise, <code>false</code>.
    :type detailed_error_logging_enabled: bool
    :param publishing_username: Publishing user name.
    :type publishing_username: str
    :param app_settings: Application settings.
    :type app_settings: list[~azure.mgmt.web.models.NameValuePair]
    :param azure_storage_accounts: User-provided Azure storage accounts.
    :type azure_storage_accounts: dict[str,
     ~azure.mgmt.web.models.AzureStorageInfoValue]
    :param connection_strings: Connection strings.
    :type connection_strings: list[~azure.mgmt.web.models.ConnStringInfo]
    :ivar machine_key: Site MachineKey.
    :vartype machine_key: ~azure.mgmt.web.models.SiteMachineKey
    :param handler_mappings: Handler mappings.
    :type handler_mappings: list[~azure.mgmt.web.models.HandlerMapping]
    :param document_root: Document root.
    :type document_root: str
    :param scm_type: SCM type. Possible values include: 'None', 'Dropbox',
     'Tfs', 'LocalGit', 'GitHub', 'CodePlexGit', 'CodePlexHg', 'BitbucketGit',
     'BitbucketHg', 'ExternalGit', 'ExternalHg', 'OneDrive', 'VSO'
    :type scm_type: str or ~azure.mgmt.web.models.ScmType
    :param use32_bit_worker_process: <code>true</code> to use 32-bit worker
     process; otherwise, <code>false</code>.
    :type use32_bit_worker_process: bool
    :param web_sockets_enabled: <code>true</code> if WebSocket is enabled;
     otherwise, <code>false</code>.
    :type web_sockets_enabled: bool
    :param always_on: <code>true</code> if Always On is enabled; otherwise,
     <code>false</code>.
    :type always_on: bool
    :param java_version: Java version.
    :type java_version: str
    :param java_container: Java container.
    :type java_container: str
    :param java_container_version: Java container version.
    :type java_container_version: str
    :param app_command_line: App command line to launch.
    :type app_command_line: str
    :param managed_pipeline_mode: Managed pipeline mode. Possible values
     include: 'Integrated', 'Classic'
    :type managed_pipeline_mode: str or
     ~azure.mgmt.web.models.ManagedPipelineMode
    :param virtual_applications: Virtual applications.
    :type virtual_applications:
     list[~azure.mgmt.web.models.VirtualApplication]
    :param load_balancing: Site load balancing. Possible values include:
     'WeightedRoundRobin', 'LeastRequests', 'LeastResponseTime',
     'WeightedTotalTraffic', 'RequestHash'
    :type load_balancing: str or ~azure.mgmt.web.models.SiteLoadBalancing
    :param experiments: This is work around for polymophic types.
    :type experiments: ~azure.mgmt.web.models.Experiments
    :param limits: Site limits.
    :type limits: ~azure.mgmt.web.models.SiteLimits
    :param auto_heal_enabled: <code>true</code> if Auto Heal is enabled;
     otherwise, <code>false</code>.
    :type auto_heal_enabled: bool
    :param auto_heal_rules: Auto Heal rules.
    :type auto_heal_rules: ~azure.mgmt.web.models.AutoHealRules
    :param tracing_options: Tracing options.
    :type tracing_options: str
    :param vnet_name: Virtual Network name.
    :type vnet_name: str
    :param cors: Cross-Origin Resource Sharing (CORS) settings.
    :type cors: ~azure.mgmt.web.models.CorsSettings
    :param push: Push endpoint settings.
    :type push: ~azure.mgmt.web.models.PushSettings
    :param api_definition: Information about the formal API definition for the
     app.
    :type api_definition: ~azure.mgmt.web.models.ApiDefinitionInfo
    :param auto_swap_slot_name: Auto-swap slot name.
    :type auto_swap_slot_name: str
    :param local_my_sql_enabled: <code>true</code> to enable local MySQL;
     otherwise, <code>false</code>. Default value: False .
    :type local_my_sql_enabled: bool
    :param managed_service_identity_id: Managed Service Identity Id
    :type managed_service_identity_id: int
    :param x_managed_service_identity_id: Explicit Managed Service Identity Id
    :type x_managed_service_identity_id: int
    :param ip_security_restrictions: IP security restrictions for main.
    :type ip_security_restrictions:
     list[~azure.mgmt.web.models.IpSecurityRestriction]
    :param scm_ip_security_restrictions: IP security restrictions for scm.
    :type scm_ip_security_restrictions:
     list[~azure.mgmt.web.models.IpSecurityRestriction]
    :param scm_ip_security_restrictions_use_main: IP security restrictions for
     scm to use main.
    :type scm_ip_security_restrictions_use_main: bool
    :param http20_enabled: Http20Enabled: configures a web site to allow
     clients to connect over http2.0. Default value: True .
    :type http20_enabled: bool
    :param min_tls_version: MinTlsVersion: configures the minimum version of
     TLS required for SSL requests. Possible values include: '1.0', '1.1',
     '1.2'
    :type min_tls_version: str or ~azure.mgmt.web.models.SupportedTlsVersions
    :param ftps_state: State of FTP / FTPS service. Possible values include:
     'AllAllowed', 'FtpsOnly', 'Disabled'
    :type ftps_state: str or ~azure.mgmt.web.models.FtpsState
    :param reserved_instance_count: Number of reserved instances.
     This setting only applies to the Consumption Plan
    :type reserved_instance_count: int
    """

    _validation = {
        'machine_key': {'readonly': True},
        'reserved_instance_count': {'maximum': 10, 'minimum': 0},
    }

    _attribute_map = {
        'number_of_workers': {'key': 'numberOfWorkers', 'type': 'int'},
        'default_documents': {'key': 'defaultDocuments', 'type': '[str]'},
        'net_framework_version': {'key': 'netFrameworkVersion', 'type': 'str'},
        'php_version': {'key': 'phpVersion', 'type': 'str'},
        'python_version': {'key': 'pythonVersion', 'type': 'str'},
        'node_version': {'key': 'nodeVersion', 'type': 'str'},
        'linux_fx_version': {'key': 'linuxFxVersion', 'type': 'str'},
        'windows_fx_version': {'key': 'windowsFxVersion', 'type': 'str'},
        'request_tracing_enabled': {'key': 'requestTracingEnabled', 'type': 'bool'},
        'request_tracing_expiration_time': {'key': 'requestTracingExpirationTime', 'type': 'iso-8601'},
        'remote_debugging_enabled': {'key': 'remoteDebuggingEnabled', 'type': 'bool'},
        'remote_debugging_version': {'key': 'remoteDebuggingVersion', 'type': 'str'},
        'http_logging_enabled': {'key': 'httpLoggingEnabled', 'type': 'bool'},
        'logs_directory_size_limit': {'key': 'logsDirectorySizeLimit', 'type': 'int'},
        'detailed_error_logging_enabled': {'key': 'detailedErrorLoggingEnabled', 'type': 'bool'},
        'publishing_username': {'key': 'publishingUsername', 'type': 'str'},
        'app_settings': {'key': 'appSettings', 'type': '[NameValuePair]'},
        'azure_storage_accounts': {'key': 'azureStorageAccounts', 'type': '{AzureStorageInfoValue}'},
        'connection_strings': {'key': 'connectionStrings', 'type': '[ConnStringInfo]'},
        'machine_key': {'key': 'machineKey', 'type': 'SiteMachineKey'},
        'handler_mappings': {'key': 'handlerMappings', 'type': '[HandlerMapping]'},
        'document_root': {'key': 'documentRoot', 'type': 'str'},
        'scm_type': {'key': 'scmType', 'type': 'str'},
        'use32_bit_worker_process': {'key': 'use32BitWorkerProcess', 'type': 'bool'},
        'web_sockets_enabled': {'key': 'webSocketsEnabled', 'type': 'bool'},
        'always_on': {'key': 'alwaysOn', 'type': 'bool'},
        'java_version': {'key': 'javaVersion', 'type': 'str'},
        'java_container': {'key': 'javaContainer', 'type': 'str'},
        'java_container_version': {'key': 'javaContainerVersion', 'type': 'str'},
        'app_command_line': {'key': 'appCommandLine', 'type': 'str'},
        'managed_pipeline_mode': {'key': 'managedPipelineMode', 'type': 'ManagedPipelineMode'},
        'virtual_applications': {'key': 'virtualApplications', 'type': '[VirtualApplication]'},
        'load_balancing': {'key': 'loadBalancing', 'type': 'SiteLoadBalancing'},
        'experiments': {'key': 'experiments', 'type': 'Experiments'},
        'limits': {'key': 'limits', 'type': 'SiteLimits'},
        'auto_heal_enabled': {'key': 'autoHealEnabled', 'type': 'bool'},
        'auto_heal_rules': {'key': 'autoHealRules', 'type': 'AutoHealRules'},
        'tracing_options': {'key': 'tracingOptions', 'type': 'str'},
        'vnet_name': {'key': 'vnetName', 'type': 'str'},
        'cors': {'key': 'cors', 'type': 'CorsSettings'},
        'push': {'key': 'push', 'type': 'PushSettings'},
        'api_definition': {'key': 'apiDefinition', 'type': 'ApiDefinitionInfo'},
        'auto_swap_slot_name': {'key': 'autoSwapSlotName', 'type': 'str'},
        'local_my_sql_enabled': {'key': 'localMySqlEnabled', 'type': 'bool'},
        'managed_service_identity_id': {'key': 'managedServiceIdentityId', 'type': 'int'},
        'x_managed_service_identity_id': {'key': 'xManagedServiceIdentityId', 'type': 'int'},
        'ip_security_restrictions': {'key': 'ipSecurityRestrictions', 'type': '[IpSecurityRestriction]'},
        'scm_ip_security_restrictions': {'key': 'scmIpSecurityRestrictions', 'type': '[IpSecurityRestriction]'},
        'scm_ip_security_restrictions_use_main': {'key': 'scmIpSecurityRestrictionsUseMain', 'type': 'bool'},
        'http20_enabled': {'key': 'http20Enabled', 'type': 'bool'},
        'min_tls_version': {'key': 'minTlsVersion', 'type': 'str'},
        'ftps_state': {'key': 'ftpsState', 'type': 'str'},
        'reserved_instance_count': {'key': 'reservedInstanceCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(SiteConfig, self).__init__(**kwargs)
        self.number_of_workers = kwargs.get('number_of_workers', None)
        self.default_documents = kwargs.get('default_documents', None)
        self.net_framework_version = kwargs.get('net_framework_version', "v4.6")
        self.php_version = kwargs.get('php_version', None)
        self.python_version = kwargs.get('python_version', None)
        self.node_version = kwargs.get('node_version', None)
        self.linux_fx_version = kwargs.get('linux_fx_version', None)
        self.windows_fx_version = kwargs.get('windows_fx_version', None)
        self.request_tracing_enabled = kwargs.get('request_tracing_enabled', None)
        self.request_tracing_expiration_time = kwargs.get('request_tracing_expiration_time', None)
        self.remote_debugging_enabled = kwargs.get('remote_debugging_enabled', None)
        self.remote_debugging_version = kwargs.get('remote_debugging_version', None)
        self.http_logging_enabled = kwargs.get('http_logging_enabled', None)
        self.logs_directory_size_limit = kwargs.get('logs_directory_size_limit', None)
        self.detailed_error_logging_enabled = kwargs.get('detailed_error_logging_enabled', None)
        self.publishing_username = kwargs.get('publishing_username', None)
        self.app_settings = kwargs.get('app_settings', None)
        self.azure_storage_accounts = kwargs.get('azure_storage_accounts', None)
        self.connection_strings = kwargs.get('connection_strings', None)
        self.machine_key = None
        self.handler_mappings = kwargs.get('handler_mappings', None)
        self.document_root = kwargs.get('document_root', None)
        self.scm_type = kwargs.get('scm_type', None)
        self.use32_bit_worker_process = kwargs.get('use32_bit_worker_process', None)
        self.web_sockets_enabled = kwargs.get('web_sockets_enabled', None)
        self.always_on = kwargs.get('always_on', None)
        self.java_version = kwargs.get('java_version', None)
        self.java_container = kwargs.get('java_container', None)
        self.java_container_version = kwargs.get('java_container_version', None)
        self.app_command_line = kwargs.get('app_command_line', None)
        self.managed_pipeline_mode = kwargs.get('managed_pipeline_mode', None)
        self.virtual_applications = kwargs.get('virtual_applications', None)
        self.load_balancing = kwargs.get('load_balancing', None)
        self.experiments = kwargs.get('experiments', None)
        self.limits = kwargs.get('limits', None)
        self.auto_heal_enabled = kwargs.get('auto_heal_enabled', None)
        self.auto_heal_rules = kwargs.get('auto_heal_rules', None)
        self.tracing_options = kwargs.get('tracing_options', None)
        self.vnet_name = kwargs.get('vnet_name', None)
        self.cors = kwargs.get('cors', None)
        self.push = kwargs.get('push', None)
        self.api_definition = kwargs.get('api_definition', None)
        self.auto_swap_slot_name = kwargs.get('auto_swap_slot_name', None)
        self.local_my_sql_enabled = kwargs.get('local_my_sql_enabled', False)
        self.managed_service_identity_id = kwargs.get('managed_service_identity_id', None)
        self.x_managed_service_identity_id = kwargs.get('x_managed_service_identity_id', None)
        self.ip_security_restrictions = kwargs.get('ip_security_restrictions', None)
        self.scm_ip_security_restrictions = kwargs.get('scm_ip_security_restrictions', None)
        self.scm_ip_security_restrictions_use_main = kwargs.get('scm_ip_security_restrictions_use_main', None)
        self.http20_enabled = kwargs.get('http20_enabled', True)
        self.min_tls_version = kwargs.get('min_tls_version', None)
        self.ftps_state = kwargs.get('ftps_state', None)
        self.reserved_instance_count = kwargs.get('reserved_instance_count', None)
