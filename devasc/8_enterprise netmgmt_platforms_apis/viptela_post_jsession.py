import requests
import sys

'''
Split this up:
1 - Get headers
2 - Get jsessionid
3 - Get token
'''


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

    sess_headers = login_response.headers
    sess_cookies = login_response.cookies

    # Gets the list of headers returned from request
    for k in sess_headers:
        print(f'{k}: {sess_headers.get(k)}')

    # Returns information on state of request
    if sess_cookies.get('JSESSIONID'):
        # Gets the cookie directly from the header
        print(f"Enjoy your tasty cookie: {sess_cookies.get('JSESSIONID')}")
        print("Login success.")
    else:
        print("Login Failed")
        print("Exiting...")
        sys.exit(0)


if __name__ == '__main__':
    login('sandbox-sdwan-1.cisco.com', 'devnetuser', 'RG!_Yw919_83')
