Common Architectural Styles
---------------------------
The application has the controlling stake in how the API interacts with 3rd parties. Unfortunately, this means that there is no standard way to create an API.
Technically each application could expose a haphazard set of calls, but fortunately a set of best practices exist. These best practices cover standards, protocols and specific styles.
This makes it easier for consumers of the API to learn & understand the API as the concepts will already be familiar.

The three most popular architectural styles are: SOAP, RPC & REST.

Remote Procedure Call (RPC):
----------------------------
This architecture is a request-response model where the originating application (client) makes a procedure call to a target application (server). The server application is typically housed on another system in the network.
The client is not aware that the call being made is to a remote endpoint as this detail is abstracted away from the client. As far as the client is concerned, the procedure calls are simply actions that it wants to perform.
This effectively means the RPC is a just a method to the client with arguments. When the method is called it is executed and the results are returned.

The most common usage of RPC is that the client makes a synchronous request to the server and is blocked while the server processes the request.
When the server is finished processing the request it sends the response back to the client, which blocks its process.

RPC can be applied to multiple transport protocols and some examples are:

- XML-RPC
- JSON-RPC
- NFS
- SOAP

Simple Object Access Protocol (SOAP):
-------------------------------------
This protocol is used as a messaging protocol for communicating between applications on different platforms. SOAP can also be used for applications communicating together that use different programming languages.
It is an XML-based protocol that was designed by Microsoft and most commonly used with HTTP transport. It is extensible to other types of transport.

SOAP has 3 defining characteristics:
- Independent
- Extensible
- Neutral

Independent:
------------
SOAP was designed with the intend in mind that all types of applications can communicate with one another. It is irrelevant how different these applications are. The applications can run on different OSs, they can use 
different programming languages and be as different as can be - SOAP doesn't care.

Extensible:
-----------
As an application of XML, SOAP can have extensions added into it. This extensibility means that you can add features like reliability and security.

Neutral:
--------
SOAP can be used over any transport protocol - HTTP, SMTP, TCP, UDP, JMS (Java Messaging Service)


SOAP Messages:
--------------
At its core SOAP is just an XML document with 4 elements:
- Envelope
- Header
- Body
- Fault

<?xml version="1.0"?>

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header/>
    <soap:Body>
        <soap:Fault>
            <faultcode>soap:Server</faultcode>
            <faultstring>Query request too large.</faultstring>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>

^ Example of a SOAP message

Envelope
        # The Envelope MUST be the root element of the XML document. In the namespace provided by the Envelope is the definition that the XML document is a SOAP message

Header
        # This is an option element but if present it must be the first child of the Envelope element.
        # Similar to other headers this section contains application-specific information
        # This information might be auth, SOAP specific attributes, or other attributes defined by the application

Body
        # This contains the actaul data to be transported to the recipient
        # Data must be in the XML format and have its own namespace

Fault
        # This is an optional element, but if used must be a child of the Body element
        # There may only be one Fault element in a SOAP message
        # This element provides error and/or status information


REpresentation State Transfer (REST):
-------------------------------------
There are 6 constraints to elements within this architecture:

- Client-Server
- Stateless
- Cache
- Uniform Interface
- Layered System
- Code-on-Demand

These 6 constraints can be applied to any protocol and when applied that determines if it is RESTful.

Client-Server
        # Client & Server should be independent of each other
        # This enables the client to be built for multiple platforms & simplifies the server side components

Stateless
        # Requests from the client to server must contain all of the information needed to make the request
        # The server cannot contain session states

Cache
        # Responses from the server must state whether response is cacheable or non-cacheable
        # If cacheable, the client can use the data from the response for later requests

Uniform Interface
        # Interface between the Client & Server should adhere to 4 principles
            - Identification of Resources: A resource must be identified in the request as an individual object to be actioned but a resource can be any information
            - Manipulation of Resource through Representations: Client receives a representation of the resource from the server. This representation must contain enough information to be manipulated by the client (e.g. it cannot just be an identifier for additional resource)
            - Self-descriptive Messages: Each message must contain all of the information for the recipient to process the message, some examples of information: protocol type, data format of the message, requested operation
            - Hypermedia as the engine of application state: Data sent by the server must include additional actions and resources available for the client to access supplemental information about the resource
Layered System
        # System is made up of different hierarchical layers in which each layer provides services only to the layers above it
        # The result is that services are only consumed from the layer below

Code-on-Demand
        # This is an optional constraint that covers the use of a REST service including executable code, or links to said code, to extend client functionality. E.g. Stripe, must use REST to make available links
        # The links would contain javascipt files that could then be downloaded and executed by the client application.
        # This makes the code more modular and eliminates the need for client developers to create and maintain separate payment-processing code
        # The nature of this constraint makes it optional due to security concerns and practicalities of traversing firewalls
