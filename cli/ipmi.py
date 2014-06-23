#!/usr/bin/env python

from igor import igor

# IPMI operation commands

@igor.group()
def ipmi():
    """IPMI operations"""

@ipmi.group()
def chassis():
    """Chassis commands"""

@chassis.command()
def power():
    """View chassis information"""

@chassis.command()
def power():
    """View or set the chassis power"""
