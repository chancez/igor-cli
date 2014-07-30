#!/usr/bin/env python

import requests
from requests.exceptions import RequestException

def make_api_request(method, config, endpoint, **kwargs):
    """Makes the Igor API request and handles 400, 401, 403
       and connection errors"""
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.request(method, config.server_url + endpoint,
                                    headers=headers, **kwargs)
        if response.status_code != requests.codes.ok and \
           response.status_code != requests.codes.created:
            if response.status_code == requests.codes.unauthorized:
                print 'It appears you haven\'t logged in or your token has \
                       expired.',
                print 'See \'igor auth\'.'
            elif response.status_code == requests.codes.forbidden:
                print 'It appears you don\'t have permission for this \
                       resource.',
                print 'See \'igor permissions\'.'
            else:
                print '[',
                try:
                    print response.json()['message'],
                except:
                    print response.text,
                print ']',
                print '(HTTP error ' + str(response.status_code) + ')'
            exit()
        return response
    except RequestException as error:
        print '[ Error connecting to the Igor API server:', config.server_url, \
              ']'
        print '(' + str(error.message) + ')'
        exit()
