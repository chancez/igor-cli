#!/usr/bin/env python

import click
import json
from igor import igor
from request_utils import make_api_request
from netrc_utils import get_credentials

# User management commands

@igor.group()
@click.pass_obj
def users(config):
    """User management operations"""

@users.command()
@click.pass_obj
def list(config):
    """Lists usernames of the available users.

    Examples:

    \b
    $ igor users list
    === Available users
    user01
    user02
    """
    response = make_api_request('GET', config, '/users')

    print "=== Available users"
    for user in response.json()['users']:
        print user['username']

@users.command()
@click.option('--username', prompt=True,
                            help='Username for this user.')
@click.option('--password', prompt='Password (typing will be hidden)',
                            hide_input=True,
                            help='Password for this user.')
@click.pass_obj
def add(config, username, password):
    """Add a new user.

    Example:

    \b
    $ igor users add
    Username: user01
    Password (typing will be hidden):
    Successfully added user01.
    """

    data = {'username': username,
            'password': password}
    response = make_api_request('POST', config, '/users',
                                data=json.dumps(data))

    print 'Successfully added ' + username + '.'

@users.command()
@click.option('--username', prompt=True,
                            help='Username of the user to delete.')
@click.pass_obj
def remove(config, username):
    """Remove a user.

    Example:

    \b
    $ igor users remove
    Username: user01
    Successfully removed user01.
    """

    response = make_api_request('DELETE', config, '/users/' + username)
    print 'Successfully removed ' + username + '.'

@users.command()
@click.option('--username', prompt=True,
                            help='Username for this user.')
@click.option('--password', prompt='Password (typing will be hidden)',
                            hide_input=True,
                            help='Password for this user.')
@click.pass_obj
def update(config, username, password):
    """Change a user's password.

    Example:

    \b
    $ igor users update --username user01 --password test
    Successfully updated user02.
    """

    data = {'username': username,
            'password': password}
    response = make_api_request('PUT', config, '/users/' + username,
                                data=json.dumps(data))

    print 'Successfully updated', username

@users.command()
@click.option('--username', prompt=True,
                            help='Username for this user.')
@click.pass_obj
def info(config, username):
    """Display user information.

    Example:

    \b
    $ igor users info --username user01
    Username: user01
    """

    response = make_api_request('GET', config, '/users/' + username)
    user_info = response.json()
    print 'Username:', user_info['username']
