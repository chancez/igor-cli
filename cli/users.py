#!/usr/bin/env python

from igor import igor

# User management commands

@igor.group()
def users():
    """User management operations"""

@users.command()
def list():
    """List existing users"""

@users.command()
def add():
    """Add a new user"""

@users.command()
def remove():
    """Remove a user"""

@users.command()
def update():
    """Update an existing user"""

@users.command()
def info():
    """Show user information"""
