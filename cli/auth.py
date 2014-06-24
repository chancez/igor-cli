#!/usr/bin/env python

import click
import requests
from igor import igor
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from netrc_utils import write_credentials, delete_credentials

# Authentication commands

@igor.group()
@click.pass_obj
def auth(config):
    """Authentication operations"""

@auth.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt='Password (typing will be hidden)',
                            hide_input=True)
@click.pass_obj
def login(config, username, password):
    """Login and obtain an authentication token.
    
    This command sends your username/password combination
    to the Igor API and obtains an authentication token (with an expiry date).
    This token is stored at ~/.netrc.

    Example of interactive login:

    \b
    $ igor auth login
    Enter your credentials:
    Email: example@osuosl.org
    Password: (typing will be hidden)
    Authentication successful.

    Example of parameterized login:

    \b
    $ igor auth login --username user --password pass
    Authentication successful.
    """

    delete_credentials(config.server_host)

    try:
        response = requests.get(config.server_url + '/login',
                                auth=(username, password))
        if response.status_code != requests.codes.ok:
            print "Authentication failed."
            exit()
    except RequestException as error:
        print 'Error connecting to the Igor API server:', config.server_url
        print error.message
        exit()

    token = response.json()['token']
    config.username = username
    config.token = token
    write_credentials(config.server_host, username, token)
    
    print "Authentication successful."

@auth.command()
@click.pass_obj
def logout(config):
    """Clear local authentication credentials from ~/.netrc.
    
    Example:
    
    \b
    $ igor auth logout
    Local credentials cleared.
    """

    config.username = None
    config.token = None
    delete_credentials(config.server_host)
    print "Local credentials cleared."

@auth.command()
@click.pass_obj
def token(config):
    """Display the API token for the currently logged-in user.
    
    Example:
    
    \b
    $ igor auth token
    eyJhbGciOiJIUzI1NiIsImV4cCI6MTQwMzY0Mjg3NSwiaWF0IjoxNDAzNjQyMjc1fQ.eyJpZCI6MX0.4pQEJ4zd3e0SudoIumxOeM60uvUbgZtCurS9_0AK4Cg
    """

    if config.token:
        print config.token
    else:
        print "No logged-in user."

@auth.command()
@click.pass_obj
def whoami(config):
    """Display the username for the currently logged-in user.
    
    Example:

    \b
    $ igor auth whoami
    root
    """

    if config.username:
        print config.username
    else:
        print "No logged-in user."
