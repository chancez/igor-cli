#!/usr/bin/env python

from igor import igor

# Authentication commands

@igor.group()
def auth():
    """Authentication operations"""

@auth.command()
def login():
    """Login and store the authentication token"""

@auth.command()
def logout():
    """Logout and delete stored tokens"""

@auth.command()
def token():
    """Display the token for the currently logged-in user"""

@auth.command()
def whoami():
    """Display the username for the currently logged-in user"""
