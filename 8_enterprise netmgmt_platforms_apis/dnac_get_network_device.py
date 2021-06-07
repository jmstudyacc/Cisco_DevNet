import requests
import json

# from the auth script get an auth token
from dnac_auth_get_key import get_auth_token


def get_network_devices(token, mac, ip):
    # note that the URL has changed here as we are not querying the system for auth
    DNAC_URL = 'https://sandboxdnac.cisco.com/api/v1/network-device'

    # calls the get_auth_token() function and saves it to the DNAC_TOKEN variable
    DNAC_TOKEN = token

    # set the headers to use the DNAC_TOKEN variable
    DNAC_HEADERS = {'X-Auth-Token': f'{DNAC_TOKEN}',
                    'content-type': 'application/json'
                    }

    # payload is an empty dictionary - this will be filled by DNAC
    payload = {}

    response = {}

    try:
        if (mac is None) and (ip is None):
            # standard process to call the API
            response = requests.get(DNAC_URL, headers=DNAC_HEADERS, data=payload)

        elif (mac is not None) and (ip is None):
            queryString = {'macAddress': f'{mac}'}
            response = requests.get(DNAC_URL, headers=DNAC_HEADERS, data=payload, params=queryString)

        elif (mac is None) and (ip is not None):
            queryString = {'managementIpAddress': f'{ip}'}
            response = requests.get(DNAC_URL, headers=DNAC_HEADERS, data=payload, params=queryString)

        else:
            queryString = {'macAddress': f'{mac}', 'managementIpAddress': f'{ip}'}
            response = requests.get(DNAC_URL, headers=DNAC_HEADERS, data=payload, params=queryString)

    except:
        print("Something went wrong!")

    if not response.json()['response']:
        raise Exception(print("Incorrect values entered for IP Address or MAC Address"))

    return json.dumps(response.json(), indent=2)


if __name__ == "__main__":
    print("Printing out unfiltered list:")
    get_network_devices(get_auth_token(), None, None)

    print("\nPrinting out list filtered by MAC Address:")
    print(get_network_devices(get_auth_token(), "00:c8:8b:80:bb:00", None))

    print("\nPrinting out list filtered by IP Address:")
    print(get_network_devices(get_auth_token(), None, "10.10.22.73"))

    print("\nPrinting out list filtered by IP Address and MAC Address:")
    get_network_devices(get_auth_token(), "00:c8:8b:80:bb:00", "10.10.22.73")