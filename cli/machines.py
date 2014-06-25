#!/usr/bin/env python

import click
import json
from igor import igor
from request_utils import make_api_request
from netrc_utils import get_credentials

# Machine management commands

@igor.group()
@click.pass_obj
def machines(config):
    """Machine management operations"""

@machines.command()
@click.pass_obj
def list(config):
    """Lists hostnames of the available machines and
    the accessible machines (that the currently logged-in user
    has permission to access).

    Examples:

    \b
    $ igor machines list
    === Available machines
    machine01
    machine02
    === Accessible machines
    machine01
    """
    response = make_api_request('GET', config, '/machines')
    current_user = get_credentials(config.server_host)[1]

    print "=== Available machines"
    for machine in response.json()['machines']:
        print machine['hostname']

    response = make_api_request('GET', config, '/users/' + current_user +
                                               '/machines')
    print "=== Accessible machines"
    for machine in response.json()['machines']:
        print machine['hostname']


@machines.command()
@click.option('--hostname', prompt=True,
                            help='The short hostname for this machine.')
@click.option('--fqdn', prompt='FQDN',
                        help='The fully qualified domain name for this machine.')
@click.option('--username', prompt=True,
                            help='The IPMI username for this machine.')
@click.option('--password', prompt='Password (typing will be hidden)',
                            hide_input=True,
                            help='The IPMI password for this machine.')
@click.pass_obj
def add(config, hostname, fqdn, username, password):
    """Add a new machine entry.

    Example:

    \b
    $ igor machines add
    Hostname: machine01
    FQDN: igor.osuosl.oob
    Username: root
    Password (typing will be hidden):
    Successfully added machine01.
    """

    data = {'hostname': hostname,
            'fqdn': fqdn,
            'username': username,
            'password': password}
    response = make_api_request('POST', config, '/machines',
                                data=json.dumps(data))

    print 'Successfully added ' + hostname + '.'

@machines.command()
@click.option('--hostname', prompt=True,
                            help='Short hostname of the machine to delete.')
@click.pass_obj
def remove(config, hostname):
    """Remove a machine entry.

    Example:

    \b
    $ igor machines remove
    Hostname: osl01
    Successfully removed osl01.
    """

    response = make_api_request('DELETE', config, '/machines/' + hostname)
    print 'Successfully removed ' + hostname + '.'

@machines.command()
@click.option('--hostname', required=True,
                            help='The short hostname for this machine.')
@click.option('--fqdn', help='The fully qualified domain name for this machine.')
@click.option('--username', help='The IPMI username for this machine.')
@click.option('--password', help='The IPMI password for this machine.')
@click.pass_obj
def update(config, hostname, fqdn, username, password):
    """Update a machine entry.

    Example:

    \b
    $ igor machines update --hostname osl02 --fqdn osl04.test
    Successfully updated osl02.
    """

    data = {}
    if fqdn:
        data['fqdn'] = fqdn
    if username:
        date['username'] = username
    if password:
        data['password'] = password

    response = make_api_request('PUT', config, '/machines/' + hostname,
                                data=json.dumps(data))

    print 'Successfully updated', hostname

@machines.command()
@click.option('--hostname', prompt=True,
                            help='The short hostname for this machine.')
@click.pass_obj
def info(config, hostname):
    """Display machine information.

    Example:

    \b
    $ igor machines info --hostname osl02
    Hostname: osl02
    FQDN: igor.osuosl.oob
    """

    response = make_api_request('GET', config, '/machines/' + hostname)
    machine_info = response.json()
    print 'FQDN:', machine_info['fqdn']
