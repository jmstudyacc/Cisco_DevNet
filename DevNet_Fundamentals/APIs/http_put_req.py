"""
A virtual library exists.
You need query what the books are in the virtual library

You've queried the books, added a book, but now it is time to UPDATE a book!
"""
# In this code a book will be intentionally added with an incorrect field
# This book will then be updated with the correct details

# Import necessary libraries
import requests
import json

url = "http://localhost:8080/v1/books"

book = {
    'name': 'The Art of Computer Programming',
    'authors': ['Donald Nuth'], 
    'date': 1968,
    'isbn': '0-201-03801-3'
    }

# Book object is defined and created, now to add it to the virtual library
# This is achieved using the same POST method as before 
response =  requests.post(url, json=book)

# Assign the response in JSON format to the 'book_data' variable
book_data = response.json()

# Test the process to see if it was added
print('------------------------------\nNEW BOOK ADDED TO THE LIBRARY\n------------------------------')
print(json.dumps(book_data, indent=4))

# You notice that there was a typo in the Author's name
# How do you resolve this? With the HTTP PUT!
# We need to access the book_data variable and change the 'authors' key
 
book_data["authors"] = ["Donald Knuth"]
update_book_url = "http://localhost:8080/v1/books/{}".format(book_data['uuid'])
response = requests.put(update_book_url, json=book_data) 