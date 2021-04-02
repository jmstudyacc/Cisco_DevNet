"""
A virtual library exists.
You need query what the books are in the virtual library

You've queried the books, added a book, updated a book and now it is time to DELETE a book!
"""
# If you want to permanently delete a resource this is achieved by using the REST API DELETE verb

import requests
import json

url = 'http://localhost:8080/v1/books'

book = {
    "name": "The Art of Computer Programming",
    "authors": [
    "Donald Knuth"
    ],
    "date": 1968,
    "isbn": "0-201-03801-3"   
    }

# Add this new book
response = requests.post(url, json=book)
book_data = response.json()
print(book_data)

# Now to delete the book that was just added

delete_book_url = 'http//localhost:8080/v1/books/{}'.format(book_data['uuid'])
response = requests.delete(delete_book_url)

print('HTTP status code after deleting the book: ', response.status_code)