#!/usr/bin/env python

"""
Author: James Miles
Purpose: As part of Nick Russo's DevNet course
I am trying to get an access token from Cisco DNA Center using REST API
"""

import requests
from requests.auth import *
from dnac_config import *
import json

"""
Now to define the function that will get the auth token.
Use requests.post to make a call to the Auth endpoint
"""

def get_auth_token():
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'   # Endpoint Cisco URL
    resp = requests.post(url, verify=False, auth=HTTPBasicAuth(DNAC_USERNAME, DNAC_PASSWORD))  # Specifying request type - POST & use vars for params 
    token = resp.json()["Token"]    # Retrieve the 'Token' from the returned JSON
    
    # If successful, print response, if failed print HTTP error
    resp.raise_for_status()
    print("Token Retrieved: {}".format(token))    # Print out the retrieved token
    return token   # Create a return statement so the token can be used again

if __name__ == "__main__":
  get_auth_token()
