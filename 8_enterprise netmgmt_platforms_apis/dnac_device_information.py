import requests
import json
from dnac_auth_get_key import get_auth_token
from dnac_get_network_device import get_network_devices

DNAC_INTERFACE_URL = 'https://sandboxdnac.cisco.com/api/v1/interface'
DNAC_TOKEN = get_auth_token()
DNAC_HEADERS = {
    'X-Auth-Token': f'{DNAC_TOKEN}',
    'content-type': 'application/json',
}


def get_device_list():
    url = 'https://sandboxdnac.cisco.com/api/v1/network-device'
    DNAC_DEVICES = get_network_devices(DNAC_TOKEN, None, None)
    response = requests.get(url, headers=DNAC_HEADERS,)
    device_list = response.json()
    get_device_id(device_list)


def get_device_id(device_json):
    for device in device_json['response']:
        print(f"Fetching Interfaces for Device ID ------> {device['id']}")
        print("\n")
        get_device_int(device['id'])
        print("\n")


def get_device_int(device_id):
    """
    Building out function to retrieve device interface - uses requests.get to make network calls to endpoint
    :param device_id:
    :return:
    """
    # dynamically builds the query parameters to get device specific interface information
    queryString = {"macAddress": device_id}
    response = requests.get(DNAC_INTERFACE_URL, headers=DNAC_HEADERS, params=queryString)
    interface_info_json = response.json()
    print_interface_info(interface_info_json)


def print_interface_info(interface_info):
    # creates the top row of table with the titles for each column
    print("{0:42}{1:10}{2:18}{3:28}{4:17}{5:10}{6:15}".
          format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))

    # loops over the info in the response but prints out in the format as denoted below
    for int in interface_info['response']:
        # {0:42} denotes available space on print out and the value to be printed is found in format(str(int['']
        print("{0:42}{1:10}{2:18}{3:28}{4:17}{5:10}{6:15}".
              format(str(int['portName']),
                     str(int['vlanId']),
                     str(int['portMode']),
                     str(int['portType']),
                     str(int['duplex']),
                     str(int['status']),
                     str(int['lastUpdated'])))


if __name__ == "__main__":
    get_device_list()
