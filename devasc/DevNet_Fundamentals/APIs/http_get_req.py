"""
A virtual library exists.
You need query what the books are in the virtual library
"""
# Import the libraries needed to run HTTP queries in Python
import requests
import json

# Now, define a var named 'url' which contains the url needed to retrieve a list of books in the virtual library
url = "http://localhost:8080/v1/books"

# The URL is defined and now you can make a GET request in Python to access the data
# The code will use the 'url' variable to send a GET request to locahost
# However, we also need to create a variable to store the data once received
# This should be done in one line
books = requests.get(url)

# You now have a variable that contains the books in the virtual library
# Print it out to check
print(books)

# Well, that wasn't very insightful, the print statement returns the HTTP code response and not the Body
# Although it is hidden from us right now, we know that the virtual library API responds with Content-Type "application/json" in the optional header field
# As it returns JSON, you can use Python to manipulate that JSON data 
# We like nice and readable, so we will take the output HTTP response data and place in a Python dictionary
print(json.dumps(books.json()))

# That's better, but still not good enough
# There's a little extra needed to make this nice and easy to read
print(json.dumps(books.json(), indent=4))