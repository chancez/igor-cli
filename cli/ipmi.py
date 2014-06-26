#!/usr/bin/env python

import click
import json
from igor import igor
from request_utils import make_api_request

# IPMI operation commands

@igor.group()
@click.pass_obj
def ipmi(config):
    """IPMI operations"""

@ipmi.group()
@click.pass_obj
def chassis(config):
    """Chassis commands"""

@chassis.command()
@click.option('--hostname', prompt=True,
                            help='The short hostname for this machine.')
@click.pass_obj
def info(config, hostname):
    """View chassis information.

    Example:

    \b
    $ igor ipmi chassis info --hostname osl01
    power_on: True
    misc_chassis_state: None
    power_restore_policy: always-on
    hostname: osl01
    power_fault: None
    main_power_fault: False
    power_control_fault: False
    power_interlock: inactive
    last_power_event: None
    power_overload: False
    """

    response = make_api_request('GET', config, '/machines/' + hostname +
                                               '/chassis')
    for key, value in response.json().iteritems():
        print key + ': ' + str(value)

@chassis.command()
@click.option('--hostname', prompt=True,
                            help='The short hostname for this machine.')
@click.option('--state', help='(on|off|reset|cycle) Desired power state.')
@click.pass_obj
def power(config, hostname, state):
    """View or set the chassis power.

    Example:

    \b
    $ igor ipmi chassis power --hostname osl01
    on

    $ igor ipmi chassis power --hostname osl01 --set cycle
    Successfully set osl01 power state to cycle.
    """

    if not state:
        response = make_api_request('GET', config, '/machines/' + hostname +
                                                   '/chassis/power')
        print response.json()['power']
    else:
        data = json.dumps({'power': state})
        response = make_api_request('POST', config, '/machines/' + hostname +
                                                    '/chassis/power', data=data)
        print 'Successfully set', hostname, 'power state to', state
