#!/usr/bin/env python

import click
import json
from igor import igor
from request_utils import make_api_request

# Permissions management commands

@igor.group()
def permissions():
    """Permission management operations"""

@permissions.command()
@click.option('--username', help='Username for the user.')
@click.option('--hostname', help='Hostname for the machine.')
@click.pass_obj
def list(config, username, hostname):
    """List accessible machines for the specified user,
    or users that can access the specified machine.

    Example:

    \b
    $ igor permissions list --username user01
    machine01
    machine02

    \b
    $ igor permissions list --hostname machine01
    user01
    user02
    """
    if (not username and not hostname) or (username and hostname):
        print 'Usage: igor permissions list [OPTIONS]'
        print
        print 'Error: Exactly one of --username or --hostname is required.'
        exit()

    if username:
        response = make_api_request('GET', config, '/users/' + username +
                                                   '/machines')
        machines = response.json()['machines']
        for machine in machines:
            print machine['hostname']
    elif hostname:
        response = make_api_request('GET', config, '/machines/' + hostname +
                                                   '/users')
        users = response.json()['users']
        for user in users:
            print user['username']

@permissions.command()
@click.option('--username', prompt=True,
                            help='Username for the user.')
@click.option('--hostname', prompt=True,
                            help='Hostname for the machine.')
@click.pass_obj
def grant(config, hostname, username):
    """Add a user-machine permission pair.

    Example:

    \b
    $ igor permissions grant
    Username: user01
    Hostname: machine01
    Permission granted successfully.
    """

    response = make_api_request('PUT', config, '/machines/' + hostname +
                                               '/users/' + username)
    print 'Permission granted successfully.'

@permissions.command()
@click.option('--username', prompt=True,
                            help='Username for the user.')
@click.option('--hostname', prompt=True,
                            help='Hostname for the machine.')
@click.pass_obj
def revoke(config, hostname, username):
    """ Remove a user-machine permission pair.

    Example:

    \b
    $ igor permissions revoke
    Username: user01
    Hostname: machine01
    Permission revoked successfully.
    """

    response = make_api_request('DELETE', config, '/machines/' + hostname +
                                                  '/users/' + username)
    print 'Permission revoked successfully.'
