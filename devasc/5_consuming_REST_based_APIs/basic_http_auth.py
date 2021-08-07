import requests, base64


def authenticate(url, username, password):
    # defining the type of auth to be used
    auth_type = 'Basic'

    # formatted the credentials as username:password
    creds = '{}:{}'.format(username, password)

    # taking the above credentials and encoding them in base64
    creds_b64 = base64.b64encode(creds)

    # headers to be passed via HTTP need to hold the auth type and the encoded credentials
    headers = {'Authorization': '{} {}'.format(auth_type, creds_b64)}

    # try block for error catching
    try:
        # a GET request using the auth credentials - provided in the HEADERS field
        response = requests.get(url, headers=headers)

        # exception catch for unsuccessful requests relating to auth errors
        if response.status_code != 200:
            raise Exception('Authentication error: {}'.format(response))

    # if the try block fails
    except Exception as e:
        print('Authentication unsuccessful! Error: {}'.format(e))

    # otherwise the block should be fine!
    print('Authentication successful!')
