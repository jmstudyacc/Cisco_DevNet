# Authentication is crucial to ensuring only the right people have access to the resource
# You need to use HTTPS/TLS if using Basic Authentication as otherwise the Username and Password is passed in plain text

# We'll access the url http://localhost:808/v1/accounts and try to pass in credentials via the Basic Auth scheme

import requests
from requests.auth import HTTPBasicAuth
import json
import sys

# This code will attempt to retrieve all of the user accounts from the library
# Since user accounts are protected only those with valid credentials should be able to view them
# admin credentials are required to access them

url = 'http://localhost:8080/v1/accounts'

# The above request is HTTP, NOT encrypted, therefore the next line is insecure
username = 'admin'
password = 'w0FimhVrty1ck9Pf2UAK4luOnkEgrDvy1VEK9iZsZOk='

# Make use of the HTTPBasicAuth class provided by the requests package
accounts = requests.get(url, auth=HTTPBasicAuth(username, password))

try:
    accounts.raise_for_status()

except requests.exceptions.HTTPError as e:
    # This code will not be run if the username and password are correct
    print('Error!: {}'.format(e))
    sys.exit()

# This code will be executed
print(accounts.status_code)