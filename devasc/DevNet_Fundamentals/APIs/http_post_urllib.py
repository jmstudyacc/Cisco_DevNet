"""
A virtual library exists.
You need query what the books are in the virtual library

You've queried the books, but now it's time to ADD a book, how do?
"""

# Perhaps you cannot download other libraries and only have the standard Python library
# You should then use the 'urllib' library that is native to Python
import urllib.request
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

# This all looks pretty similar to the 'requests' library, but here is where things change

payload = json.dumps(book).encode('utf8')
request = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
response = urllib.request.urlopen(request)
print(response.status)

# As you can see there is a lot more configuration on your behalf with the urllib library
# In fact, that neat autopopulate of the 'Content-Type' header is lost when using urllib
# There is more syntax and some of it is less intuitive than the 'requests' library