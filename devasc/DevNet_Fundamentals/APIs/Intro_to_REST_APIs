REST Web Service APIs
---------------------
A REST web service API (REST API) is a programming interface that communicates over HTTP while adhering to the principles of the REST architectural style.

To refresh your memory, the six principles of the REST architectural style are:

    Client-Server
    Stateless
    Cache
    Uniform Interface
    Layered System
    Code-On-Demand (Optional)

Since REST APIs communicate over HTTP, they use the same concepts as the HTTP protocol, such as:

    HTTP requests/responses
    HTTP verbs
    HTTP status codes
    HTTP headers/body

REST API Requests:
------------------
REST API requests are essentially HTTP requests that follow REST principles. These requests are a way for the client to ask the server to perform a function.
Since it is an API these functions are pre-defined by the server and the client must follow the specification provided by the server.

REST APIs are made up of 4 major components:
- Uniform Resource Identifier (URI)
- HTTP Method
- Header
- Body

Uniform Resource Identifier:
        # This identifies which resource the client wants to modify. This is a key requirement of REST as the resource must be identified.
        # It is essentially the same format as a URL, with the following components in the specific order: Scheme, Authority, Path, Query

        Scheme
                # This specifies which HTTP protocol should be used, for a REST API, the 2 options are:
                    - http, the connection is open
                    - https, the connection is secure
        Authority
                # The authority or destination, consists of two parts that are preceded by 2 forward slashes:
                    - Host
                    - Port

                # The host is the name, or IP address of the server providing the REST API service
                # The port is the communication endpoint that is associated with the host

        Path
                # For a REST API the path is usually known as the resource path and represents the location of the resource
                # The path is preceded by a forward slash / and can consist of multiple segments separated by /
        
        Query
                # This is an optional parameter
                # The query provides additional details for scope, for filtering or to clarify a request
                # If a query is present it is preceded by ?
                # There is not a specific syntax for query parameters but it is typically defined as a set of key-value pairs separated by &

HTTP Method:
        # REST APIs leverage standard HTTP methods, known as HTTP verbs as a means to tell the service which action is requested
        # There isn't a standard mapping which HTTP method is mapped to which action
        # The suggested mapping looks like:

        HTTP Method 	Action 	        Description
        ----------------------------------------------------------------------------------
            POST 	    Create 	        Create a new object or resource.
            GET 	    Read 	        Retrieve resource details from the system.
            PUT 	    Update 	        Replace or update an existing resource.
            PATCH 	    Partial Update 	Update some details from an existing resource.
            DELETE 	    Delete 	        Remove a resource from the system.

Header:
        # REST APIs use the standard HTTP header format to communicate additional information between the client and server - however this additional information is optional
        # HTTP headers are formatted as name-value pairs that are separated by a colon : e.g. [name]:[value]
        # Some standard HTTP headers are defined, but the web service accepting the REST API request can define custom headers to accept

        # There are 2 Types of Headers:
                # Request headers: these include additional information that doesn't relate to the content of the message. The following is a typical Request Header you may find for a REST API:

                Key 	        Example Value 	            Description
                ------------------------------------------------------------------------------------------
                Authorization 	Basic dmFncmFudDp2YWdyYW50 	Provide credentials to authorize the request

                # Entity headers: additional information that describes the content of the body of the message, a typical entity header may look like:

                Key 	        Example Value 	            Description
                --------------------------------------------------------------------------------
                Content-Type 	application/json 	Specify the format of the data in the body

Body:
        # Body of the REST API request contains all of the data pertaining to the URI
        # REST API requests that use the HTTP methods of, POST, PUT, PATCH typically include a body
        # Depending on the HTTP method, the body is optional
        # If the body IS used the data type must be specified in the entity header using the Content-Type key

REST API Responses:
-------------------