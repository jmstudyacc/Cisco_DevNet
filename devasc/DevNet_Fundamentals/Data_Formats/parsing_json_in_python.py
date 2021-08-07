# Frequently you will find JSON and YAML used to communicate with a REST interface
# An example that will be used here is parsing a response from a token request

"""
{
 "access_token":"ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3",
 "expires_in":1209600,
 "refresh_token":"MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4",
 "refreshtokenexpires_in":7776000
}
"""

# Python has its own json library which can be used to PARSE data from JSON into 
# native Python data structures. It is also capable of SERIALIZING the data back out into JSON.


# Import the JSON and YAML libraries into Python
import json
import yaml

# First you want to load the JSON file into a string, using the json.load() method
with open('myfile.json', 'r') as json_file:
    our_json = json.load(json_file)

# After passing in the JSON data to be read, remember to close the file
json_file.close()
print(our_json)

# You will now read a SET of JSON key:value pairs
# You can specify what you want to receive by add a key of interest
print(our_json['expires_in'])

# You can then interpolate data into the print statement to make the responses clearer
print("The access token from JSON is: %s" % our_json['access_token'])

"""
Your output should look like:

{'access_token': 'ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3', 'expires_in': 1209600, 'refresh_token': 'MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4', 'refreshtokenexpires_in': 7776000} 
1209600
The access token from JSON is: ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3

If you want to, and you may need to in some instances, you can interchange JSON with YAML with:

yaml.dump() function
"""

# Remember YAML needs 3 dashses to start a YAML file, so include these in your print statement
print("\n\n---")

print(yaml.dump(our_json))      # We have identified the data with the JSON library and then dump it into YAML