import requests


def checkStatus(url):
    # Tries to check the API status
    try:
        # using the requests module you send a get request to the passed url with the API status page
        status = requests.get(url + "/api/status")
        # if the status returned is not 200 - all good - an error should be raised
        if status.status_code != 200:
            # raises the exception and provides feedback to the user
            raise Exception("Unexpected status code: " + status.status_code)

    # if the try block failed the error needs to also be captured
    except Exception as e:
        print("API endpoint encounter an error: " + e)