#!/usr/bin/env python

import click
import ConfigParser
from os.path import expanduser
from netrc_utils import get_credentials

class Config(object):
    def __init__(self, server_url, server_host, server_port,
                 username, token, verbose):
        self.server_url = server_url
        self.server_host = server_host
        self.server_port = server_port
        self.username = username
        self.token = token
        self.verbose = verbose
        
@click.group()
@click.option('--igor-server', envvar='IGOR_SERVER', default='',
                               metavar='URL',
                               help='URL as host:port of the Igor API server')
@click.option('--verbose', envvar='IGOR_VERBOSE', is_flag=True,
                           default=False, help='Print verbose information')
@click.pass_context
def igor(ctx, igor_server, verbose):
    """The Igor CLI. Connects to an Igor API server to perform
       IPMI, user and machine management operations.
       
       See 'igor COMMAND --help' for more information on a specific command."""

    # If not provided, try to read from the config file
    if not igor_server:
        config = ConfigParser.RawConfigParser()
        files = config.read(expanduser('~/.igorrc'))
        if len(files) > 0:
            try:
                igor_server = config.get('igor', 'igor_server')
            except ConfigParser.Error:
                pass

    # Store the Igor API server host and port separately for convenience
    server_url = 'http://' + igor_server
    server_url_parts = igor_server.split(':')
    server_host = server_url_parts[0]
    server_port = server_url_parts[1]

    # Attempt to read login information from ~/.netrc
    username, token = get_credentials(server_host)
 
    ctx.obj = Config(server_url, server_host, server_port,
                     username, token, verbose) 
