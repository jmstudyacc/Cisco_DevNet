import requests
import json

# use a REST-API endpoint that you can freely reach
url = "http://jsonplaceholder.typicode.com/users/1"

# the url here specifies that we are accessing a specific user, user/1
response = requests.get(url=url, params=None)
status_code = response.status_code
content = json.loads(response.content)

print(f'Status code: {status_code}')
print(f'Response content: {content}')

# here the request is actually to a collection and not a specific record
url = "http://jsonplaceholder.typicode.com/users"

# the code stays exactly the same though!
response = requests.get(url=url, params=None)
status_code = response.status_code
content = json.loads(response.content)

print(f'Status code: {status_code}')
print(f'Response content: {content}')
