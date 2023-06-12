# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190111

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.usage.src.oci_cli_usage.generated import usage_service_cli


@click.command(cli_util.override('usagelimits.usagelimits_root_group.command_name', 'usagelimits'), cls=CommandGroupWithAlias, help=cli_util.override('usagelimits.usagelimits_root_group.help', """Use the Usage Proxy API to list Oracle Support Rewards, view related detailed usage information, and manage users who redeem rewards. For more information, see [Oracle Support Rewards Overview]."""), short_help=cli_util.override('usagelimits.usagelimits_root_group.short_help', """Usage Proxy API"""))
@cli_util.help_option_group
def usagelimits_root_group():
    pass


@click.command(cli_util.override('usagelimits.usage_limit_summary_group.command_name', 'usage-limit-summary'), cls=CommandGroupWithAlias, help="""Encapsulates a collection of Hard and Soft Limits for a resource within a subscription.""")
@cli_util.help_option_group
def usage_limit_summary_group():
    pass


usage_service_cli.usage_service_group.add_command(usagelimits_root_group)
usagelimits_root_group.add_command(usage_limit_summary_group)


@usage_limit_summary_group.command(name=cli_util.override('usagelimits.list_usage_limits.command_name', 'list-usage-limits'), help=u"""Returns the list of usage limit for the subscription ID and tenant ID. \n[Command Reference](listUsageLimits)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--subscription-id', required=True, help=u"""The subscription ID for which rewards information is requested for.""")
@cli_util.option('--limit-type', help=u"""Hard or soft limit. Hard limits lead to breaches, soft to alerts.""")
@cli_util.option('--resource-type', help=u"""Resource Name.""")
@cli_util.option('--service-type', help=u"""Service Name.""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in the paginated response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, which can be ascending (ASC) or descending (DESC).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "TIMESTART"]), help=u"""The field to sort by. Supports one sort order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage', 'class': 'UsageLimitCollection'})
@cli_util.wrap_exceptions
def list_usage_limits(ctx, from_json, all_pages, page_size, compartment_id, subscription_id, limit_type, resource_type, service_type, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit_type is not None:
        kwargs['limit_type'] = limit_type
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if service_type is not None:
        kwargs['service_type'] = service_type
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage', 'usagelimits', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_usage_limits,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_usage_limits,
            limit,
            page_size,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    else:
        result = client.list_usage_limits(
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
