import time
import requests


def getUsers(url):
    # a client using this method can attempt 10 times to read the users before max is hit
    max_retries = 10

    # a timeout of 30 seconds between each try
    timeout = 30

    # loop until you hit the max_retries value
    for retry_count in range(max_retries):
        try:
            # get request to the appropriate API endpoint
            api_users = requests.get(url + "/api/users")

        # if try block fails, raise an exception and loop again
        except Exception as e:
            print("Error encountered while reading users. Retrying...")

        # if the get request comes back as 200 then return the users from /api/users
        if api_users.status_code == 200:
            # this is a bad return as it does not validate the content before returning
            return api_users

        # otherwise sleep for the specified timeout period
        else:
            time.sleep(timeout)

    # if you break out the loop due to failure you will hit this exception
    raise Exception("Retry limit reached!")