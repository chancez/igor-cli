#!/usr/bin/env python

import netrc
from os.path import expanduser

def get_credentials(host):
    """Returns the username, token for the specified host"""
    netrc_hosts = netrc.netrc().hosts
    if host in netrc_hosts:
        return netrc_hosts[host][0], netrc_hosts[host][2]
    return None, None

def delete_credentials(host):
    """Removes the credentials for the specified host from the ~/.netrc file"""
    netrc_hosts = netrc.netrc().hosts
    if host in netrc_hosts:
        del netrc_hosts[host]
        write_netrc(netrc_hosts)

def write_credentials(host, username, token):
    """Writes the host, username, token triple to the ~/.netrc file"""
    netrc_hosts = netrc.netrc().hosts
    netrc_hosts[host] = (username, None, token)
    write_netrc(netrc_hosts)
    
def write_netrc(netrc_hosts):
    """Saves the key value pairs in the provided dictionary to ~/.netrc"""
    with open(expanduser('~/.netrc'), 'w') as f:
        f.truncate()
        for host, host_info in netrc_hosts.iteritems():
            f.write('machine ' + host + '\n')
            if host_info[0]:
                f.write('\tlogin ' + host_info[0] + '\n')
            if host_info[1]:
                f.write('\taccount ' + host_info[1] + '\n')
            if host_info[2]:
                f.write('\tpassword ' + host_info[2] + '\n')
