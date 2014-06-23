#!/usr/bin/env python

from igor import igor

# Machine management commands

@igor.group()
def machines():
    """Machine management operations"""

@machines.command()
def list():
    """List the available machines"""

@machines.command()
def add():
    """Add a new machine entry"""

@machines.command()
def remove():
    """Remove a machine entry"""

@machines.command()
def update():
    """Update a machine entry"""

@machines.command()
def info():
    """Display machine information"""
