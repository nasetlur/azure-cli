# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType

from azure.cli.command_modules.rdbms._client_factory import (
    cf_mariadb_servers,
    cf_mariadb_db,
    cf_mariadb_firewall_rules,
    cf_mariadb_virtual_network_rules_operations,
    cf_mariadb_config,
    cf_mariadb_log,
    cf_mysql_servers,
    cf_mysql_db,
    cf_mysql_firewall_rules,
    cf_mysql_virtual_network_rules_operations,
    cf_mysql_config,
    cf_mysql_log,
    cf_mysql_replica,
    cf_postgres_servers,
    cf_postgres_db,
    cf_postgres_firewall_rules,
    cf_postgres_virtual_network_rules_operations,
    cf_postgres_config,
    cf_postgres_log,
    cf_postgres_replica)


# pylint: disable=too-many-locals, too-many-statements, line-too-long
def load_command_table(self, _):

    rdbms_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.rdbms.custom#{}')

    mariadb_servers_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mariadb.operations#ServersOperations.{}',
        client_factory=cf_mariadb_servers
    )

    mysql_servers_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mysql.operations#ServersOperations.{}',
        client_factory=cf_mysql_servers
    )

    postgres_servers_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.postgresql.operations#ServersOperations.{}',
        client_factory=cf_postgres_servers
    )

    mysql_replica_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mysql.operations#ReplicasOperations.{}',
        client_factory=cf_mysql_replica
    )

    postgres_replica_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.postgresql.operations#ReplicasOperations.{}',
        client_factory=cf_postgres_replica
    )

    mariadb_firewall_rule_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mariadb.operations#FirewallRulesOperations.{}',
        client_factory=cf_mariadb_firewall_rules
    )

    mysql_firewall_rule_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mysql.operations#FirewallRulesOperations.{}',
        client_factory=cf_mysql_firewall_rules
    )

    postgres_firewall_rule_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.postgresql.operations#FirewallRulesOperations.{}',
        client_factory=cf_postgres_firewall_rules
    )

    mariadb_vnet_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mariadb.operations#VirtualNetworkRulesOperations.{}',
        client_factory=cf_mariadb_virtual_network_rules_operations
    )

    mysql_vnet_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mysql.operations#VirtualNetworkRulesOperations.{}',
        client_factory=cf_mysql_virtual_network_rules_operations
    )

    postgres_vnet_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.postgresql.operations#VirtualNetworkRulesOperations.{}',
        client_factory=cf_postgres_virtual_network_rules_operations
    )

    mariadb_config_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mariadb.operations#ConfigurationsOperations.{}',
        client_factory=cf_mariadb_config
    )

    mysql_config_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mysql.operations#ConfigurationsOperations.{}',
        client_factory=cf_mysql_config
    )

    postgres_config_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.postgresql.operations#ConfigurationsOperations.{}',
        client_factory=cf_postgres_config
    )

    mariadb_log_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mariadb.operations#LogFilesOperations.{}',
        client_factory=cf_mariadb_log
    )

    mysql_log_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mysql.operations#LogFilesOperations.{}',
        client_factory=cf_mysql_log
    )

    postgres_log_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.postgresql.operations#LogFilesOperations.{}',
        client_factory=cf_postgres_log
    )

    mariadb_db_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mariadb.operations#DatabasesOperations.{}',
        client_factory=cf_mariadb_db
    )

    mysql_db_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.mysql.operations#DatabasesOperations.{}',
        client_factory=cf_mysql_db
    )

    postgres_db_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.rdbms.postgresql.operations#DatabasesOperations.{}',
        client_factory=cf_postgres_db
    )

    with self.command_group('mariadb server', mariadb_servers_sdk, client_factory=cf_mariadb_servers) as g:
        g.custom_command('create', '_server_create')
        g.custom_command('restore', '_server_restore', supports_no_wait=True)
        g.custom_command('georestore', '_server_georestore', supports_no_wait=True)
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.custom_command('list', '_server_list_custom_func')
        g.generic_update_command('update',
                                 getter_name='_server_update_get', getter_type=rdbms_custom,
                                 setter_name='_server_update_set', setter_type=rdbms_custom, setter_arg_name='parameters',
                                 custom_func_name='_server_update_custom_func')
        g.custom_wait_command('wait', '_server_mariadb_get')
        g.command('restart', 'restart')

    with self.command_group('mysql server', mysql_servers_sdk, client_factory=cf_mysql_servers) as g:
        g.custom_command('create', '_server_create')
        g.custom_command('restore', '_server_restore', supports_no_wait=True)
        g.custom_command('georestore', '_server_georestore', supports_no_wait=True)
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.custom_command('list', '_server_list_custom_func')
        g.generic_update_command('update',
                                 getter_name='_server_update_get', getter_type=rdbms_custom,
                                 setter_name='_server_update_set', setter_type=rdbms_custom, setter_arg_name='parameters',
                                 custom_func_name='_server_update_custom_func')
        g.custom_wait_command('wait', '_server_mysql_get')
        g.command('restart', 'restart')

    with self.command_group('postgres server', postgres_servers_sdk, client_factory=cf_postgres_servers) as g:
        g.custom_command('create', '_server_create')
        g.custom_command('restore', '_server_restore', supports_no_wait=True)
        g.custom_command('georestore', '_server_georestore', supports_no_wait=True)
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.custom_command('list', '_server_list_custom_func')
        g.generic_update_command('update',
                                 getter_name='_server_update_get', getter_type=rdbms_custom,
                                 setter_name='_server_update_set', setter_type=rdbms_custom, setter_arg_name='parameters',
                                 custom_func_name='_server_update_custom_func')
        g.custom_wait_command('wait', '_server_postgresql_get')
        g.command('restart', 'restart')

    with self.command_group('mysql server replica', mysql_replica_sdk) as g:
        g.command('list', 'list_by_server')

    with self.command_group('mysql server replica', mysql_servers_sdk, client_factory=cf_mysql_servers) as g:
        g.custom_command('create', '_replica_create', supports_no_wait=True)
        g.custom_command('stop', '_replica_stop', confirmation=True)

    with self.command_group('postgres server replica', postgres_replica_sdk) as g:
        g.command('list', 'list_by_server')

    with self.command_group('postgres server replica', postgres_servers_sdk, client_factory=cf_postgres_servers) as g:
        g.custom_command('create', '_replica_create', supports_no_wait=True)
        g.custom_command('stop', '_replica_stop', confirmation=True)

    with self.command_group('mariadb server firewall-rule', mariadb_firewall_rule_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')
        g.generic_update_command('update',
                                 getter_name='_firewall_rule_custom_getter', getter_type=rdbms_custom,
                                 setter_name='_firewall_rule_custom_setter', setter_type=rdbms_custom, setter_arg_name='parameters',
                                 custom_func_name='_firewall_rule_update_custom_func')

    with self.command_group('mysql server firewall-rule', mysql_firewall_rule_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')
        g.generic_update_command('update',
                                 getter_name='_firewall_rule_custom_getter', getter_type=rdbms_custom,
                                 setter_name='_firewall_rule_custom_setter', setter_type=rdbms_custom, setter_arg_name='parameters',
                                 custom_func_name='_firewall_rule_update_custom_func')

    with self.command_group('postgres server firewall-rule', postgres_firewall_rule_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')
        g.generic_update_command('update',
                                 getter_name='_firewall_rule_custom_getter', getter_type=rdbms_custom,
                                 setter_name='_firewall_rule_custom_setter', setter_type=rdbms_custom, setter_arg_name='parameters',
                                 custom_func_name='_firewall_rule_update_custom_func')

    with self.command_group('mariadb server vnet-rule', mariadb_vnet_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete')
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')
        g.generic_update_command('update')

    with self.command_group('mysql server vnet-rule', mysql_vnet_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete')
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')
        g.generic_update_command('update')

    with self.command_group('postgres server vnet-rule', postgres_vnet_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete')
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')
        g.generic_update_command('update')

    with self.command_group('mariadb server configuration', mariadb_config_sdk) as g:
        g.command('set', 'create_or_update')
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')

    with self.command_group('mysql server configuration', mysql_config_sdk) as g:
        g.command('set', 'create_or_update')
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')

    with self.command_group('postgres server configuration', postgres_config_sdk) as g:
        g.command('set', 'create_or_update')
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')

    with self.command_group('mariadb server-logs', mariadb_log_sdk, client_factory=cf_mariadb_log) as g:
        g.custom_command('list', '_list_log_files_with_filter')
        g.custom_command('download', '_download_log_files')

    with self.command_group('mysql server-logs', mysql_log_sdk, client_factory=cf_mysql_log) as g:
        g.custom_command('list', '_list_log_files_with_filter')
        g.custom_command('download', '_download_log_files')

    with self.command_group('postgres server-logs', postgres_log_sdk, client_factory=cf_postgres_log) as g:
        g.custom_command('list', '_list_log_files_with_filter')
        g.custom_command('download', '_download_log_files')

    with self.command_group('mariadb db', mariadb_db_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')

    with self.command_group('mysql db', mysql_db_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')

    with self.command_group('postgres db', postgres_db_sdk) as g:
        g.command('create', 'create_or_update')
        g.command('delete', 'delete', confirmation=True)
        g.show_command('show', 'get')
        g.command('list', 'list_by_server')

    with self.command_group('postgres',postgres_servers_sdk) as g:
        g.custom_command('get-access-token', '_get_access_token')
