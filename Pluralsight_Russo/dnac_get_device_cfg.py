#!/usr/bin/env/python

"""
Author: James Miles
Purpose: Continuing the training from Nick Russo's Pluralsight course
this script is to get a list of devices running in Cisco Sandbox DNAC
"""

import requests
from requests.auth import HTTPBasicAuth
from auth_token import get_auth_token
import json

"""
Need to define the function that will run the script.
This is usually called main()
"""

def main():
  #Get token from previously created script
  token = get_auth_token()

  # Define local variables for reuse
  api_path="https://sandboxdnac.cisco.com/dna"
  
  # Provide header information using JSON and X-Auth-Token 
  hdrs= {'X-Auth-Token': token, 'Content-Type' : 'application/json'}
  
  # Issue GET request to get list of network devices
  get_resp = requests.get(
		f"{api_path}/intent/api/v1/network-device", headers=hdrs, verify=False
		)
  # Convert output to JSON and Print
  print(json.dumps(get_resp.json(), indent=2))









if __name__ == "__main__":
    main()
