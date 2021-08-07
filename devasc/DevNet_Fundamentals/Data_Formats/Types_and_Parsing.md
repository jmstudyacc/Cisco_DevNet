
The Top 3 formats to exchange information with remote APIs are:

- XML
- JSON
- YAML

JSON and YAML are closely related, with YAML being a superset of JSON. This means any JSON script is usable in YAML, but not all of YAML is usable in JSON (but a lot is!).
XML is far older than JSON and YAML which brings difficulties. However, the tooling for XML is more robust and mature.

Parsing these data formats is pretty common when interacting with REST interfaces. The pattern of activity is typically:

- AUTHENTICATE, usually by POST'ing the user credentials and retrieving an expiring token for use in authenticating subsequent requests
- EXECUTE, a GET request to a given endpoint to retrieve a state of a resource requesting a format of, XML, JSON or YAML for the output
- MODIFY, the returned XML, JSON or YAML
- EXECUTE, a POST (or PUT) request to the given endpoint to change the state of a resource and requesting XML, JSON or YAML as the output message

PARSING:
--------

Parsing a message requires it be broken down, analysed and understood. The transmission of data between computers needs to be finished and recompiled to be understood.
This data needs to be passed into a semantically-equivalent-data structure to the receiving application. The resource can then be presented. If this semantically-equivalent-data structure is not available
you will not be able to view the data. Ever tried opening an .xlsx in Notepad?

You may have the following stored in a Python file to authenticate to a REST API.

auth = {
    "user": {
        "username": "myemail@adomain.com",
        "key": "087512348973492386"
    }
}

However, the REST API requires that the values be presented in an XML format. The above format does not satisfy that as it is in a JSON/Dictionary format. 
Working around this requires the information be SERIALIZED into XML and this can be done with a Python library. E.g., use the dicttoxml SERIALIZATION library

When the API responds it is likely to respond in the XML format. Python will then need to PARSE the received information into a format that can be accessed conveniently. E.g., use the untangle xml parser library to PARSE.