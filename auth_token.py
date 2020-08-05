#!/usr/bin/env python

"""
Author: James Miles
Purpose: As part of Nick Russo's DevNet course
I am trying to get an access token from Cisco DNA Center using REST API
"""

import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

"""
Now to define the function that will get the auth token.
Use requests.post to make a call to the Auth endpoint
"""

def get_auth_token():
    url: 'https://https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token' # Endpoint Cisco URL
    resp = request.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))    # Specifying request type - POST & use vars for params
    token = resp.json()['Token']    # Retrieve the 'Token' from the returned JSON
    print("Token Retrieved: {}".format(token))    # Print out the retrieved token
    return token   # Create a return statement so the token can be used again
