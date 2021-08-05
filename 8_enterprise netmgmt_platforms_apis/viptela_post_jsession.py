import requests
import sys
import json


def login(vmanage_ip, username, password):
    """Login to vManage"""
    base_url = f'https://{vmanage_ip}'
    login_action = '/j_security_check'
    login_url = base_url + login_action

    # Provides the username and password in dictionary format
    login_data = {'j_username': username, 'j_password': password}

    # Creates an HTTP session for HTTP verb usage
    sess = requests.session()

    # If vManage has a certificate signed by a trusted authority change verify to True
    login_response = sess.post(url=login_url, data=login_data, verify=False)

    if login_response.status_code == 200:
        print(login_response.status_code)
        print("Login success.")
    else:
        print("Login Failed")
        sys.exit(0)


if __name__ == '__main__':
    login('sandbox-sdwan-1.cisco.com', 'devnetuser', 'RG!_Yw919_83')
