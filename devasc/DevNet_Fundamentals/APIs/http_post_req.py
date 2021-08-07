"""
A virtual library exists.
You need query what the books are in the virtual library

You've queried the books, but now it's time to ADD a book, how do?
"""

# Import the required libraries, as per usual
import requests
import json

# Define the URL variable which will be used to hold the target server

url = "http://localhost:8080/v1/books"      # Note this is a STRING

"""
Adding a book is harder than just getting a book
You need to know the required fields and how these are formatted
That can usually be found out by consulting the documentation for the API
In this case the following is needed:
 - Book name e.g. 'The Art of Computer Programming'
 - Book author e.g. 'Donald Knuth'
 - Publish Date e.g. 1968
 - Book ISBN e.g. "0-201-03801-3"
The above details builds the minium for a book in the virtual library
As we are using JSON, we will represent this information in a dictionary
N.B. Pay close attention to the data types represented, we have Strings of Letters, Integers and Strings of Numbers - If you use an incorrect data type the POST request will ultimately fail!
"""

book = {                        # Think of this book as an object we are creating and defining
    'name': 'The Art of Computer Programming',
    'authors': 'Donald Knuth',
    'date': 1968,
    'isbn': '0-201-03801-3'
    }

# The new book object has been created and defined, now we need to send this book object from our local device to the remote target
# This is handled by the ol' trusty HTTP POST request, which uses similar syntax to the HTTP GET request previously configured
# A named param, 'json' is used in the POST request and we pass the Python dictionary 'book' to the 'json' param
# By supplying the 'json' param the 'requests' package will automatically handle the DESERIALIZATION of the dictionary
# It will also set the Content-Type header to application/json

# 'Response' var is assigned to the HTTP POST request, post accepts the url variable for the target and the named param for the DESERIALIZATION
response = requests.post(url, json=book)

# Prints a status code to determine success or not!
print(response.status_code)

# You should receive 200 for a successful status code