# Not as native as JSON, but still good is YAML
# You will have to ensure that your client has PyYAML installed to leverage YAML
# This is achieved easily with a pip install PyYAML

"""
The following code uses PyYAML to PARSE a YAML file, extract & print data values and
output a JSON version of the file. The method:

safe_load()

Is used to PARSE the file stream and normal PYTHON data references to extract
values from the resulting Python data structure. Python then uses the JSON module:

dumps()

To SERIALIZE the Python data back out as JSON to the terminal
"""
import json
import yaml

# Open the YAML file
yaml_file = open('myfile.yaml', 'r')

# Convert the YAML data into Python objects to benefit investigation & analysis
pythondata = yaml.safe_load(yaml_file)

# Attempt to access the same data as was accessed in the JSON version of this code
print(pythondata['expires_in'])

# Use the f-string interpolation on the access token to include it in the print statement
access_token = pythondata['access_token']
print(f"The access token from YAML is: {access_token}")

# The above works as Python takes the YAML data and makes it into a list containing the key:val pairs
# If you want to, it is possible to convert that into JSON and print the data out
print('\n\n')

# Now call the json.dumps() function to turn the 'pythondata' variable into JSON
print(json.dumps(pythondata))     # In the JSON example we used yaml.dump() here we use the json.dumps() equiv.