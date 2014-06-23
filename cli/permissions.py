#!/usr/bin/env python

from igor import igor

# Permissions management commands

@igor.group()
def permissions():
    """IPMI operations"""

@permissions.command()
def add():
    """ Add a user-machine permission pair"""

@permissions.command()
def remove():
    """ Remove a user-machine permission pair"""
