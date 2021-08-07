import requests


# this is creating a POST request to the server so the structure is a little bit different
# you will notice some new variables not used before with the get requests

def createUser(url, name, age):
    # creating a dict object that contains the parameter 'X-Api-Key' and associated value
    headers = {'X-Api-Key': '21xjwe639yk78er9'}
    payload = {'user': {'name': name, 'age': age}}

    try:
        # tries to create and POST a request to the destination URL - notice how this request contains headers & payload
        response = requests.post(url, headers=headers, data=payload)

        # authentication check - 401
        if response.status_code == 401:
            raise Exception("API Key is invalid!")

        # authorisation check - 403
        elif response.status_code == 403:
            raise Exception("API Key is not authorised!")

        # catch all error message 
        elif response.status_code != 200:
            raise Exception("API error: {}".format(response))
    except Exception as e:
        print("User creation failed! Error: {}".format(e))

    print("User {} created successfully!".format(name))

