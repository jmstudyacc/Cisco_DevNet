import configparser

import requests


def api_call(context, result_limit=10):
    config = configparser.read('api_key.ini')
    api_key = config['api_key']
    # url is read from the application context - this represents the runtime configuration of the application
    # application context usually contains data that will be different e.g. IP addresses, names, credentials etc.
    url = context.url

    # ensure your credentials are ALWAYS passed in the header or body of the POST
    cookies = {'cookies': 'api_key={}'.format(api_key)}
    body = {'limit': result_limit}

    response = requests.get(url, cookies=cookies, data=body)

    if response.status_code != 200:
        raise Exception('API call error: {}'.format(response))
    else:
        return response.data

