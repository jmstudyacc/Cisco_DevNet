import requests
import json

MERAKI_X_AUTH = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
MERAKI_NET_ID = 'L_783626335162466320'
MERAKI_URL = f'https://api.meraki.com/api/v1/networks/{MERAKI_NET_ID}/wireless/ssids'

# payload is an empty dictionary
payload = {}

# define the necessary headers for Meraki
headers = {'X-Cisco-Meraki-API-Key': MERAKI_X_AUTH,
           'Accept': 'application/json',
           'Content-type': 'application/json'
           }

# create a variable to store the response of upcoming request
response = requests.request('GET', url=MERAKI_URL, headers=headers, data=payload)

# print the status code and the response itself
print(response.status_code)

# print out the resulting networks
print(json.dumps(response.json(), indent=2))