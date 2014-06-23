#!/usr/bin/env python

import click

class Config(object):
    def __init__(self, server, verbose):
        self.verbose = verbose
        self.server = server

@click.group()
@click.option('--igor-server', envvar='IGOR_SERVER', default='',
              metavar='URL', help='URL of the Igor API server')
@click.option('--verbose', envvar='IGOR_VERBOSE', is_flag=True,
              default=False, help='Print verbose information')
@click.pass_context
def igor(ctx, igor_server, verbose):
    """The Igor CLI. Connects to an Igor API server to perform
       IPMI, user and machine management operations.
       
       See 'igor COMMAND --help' for more information on a specific command."""
    ctx.obj = Config(igor_server, verbose)
