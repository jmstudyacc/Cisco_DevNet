import requests
import json


def get_auth_token():
    DNAC_USER = ''
    DNAC_PASS = ''
    DNAC_HEADERS = {'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE'}

    # DNAC Endpoint URL
    DNAC_URL = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'

    # Create the POST request - verify set to False as this is an HTTPS connection
    response = requests.post(DNAC_URL, headers=DNAC_HEADERS,)# verify=False)

    # retrieves the token from the returned JSON
    token = response.json()['Token']

    # print out of the Token, but this is unnecessary
    # print(f'Token retrieved: {token}')

    # return the Token for use by other scripts
    return token


# including this to allow the script to run or be a module
if __name__ == "__main__":
    get_auth_token()
