Types of Design Styles
----------------------
APIs can be delivered primarily in 2 ways - synchronously or a-synchronously. It is important to determine which way it is delivered as this impacts manner the API handles responses.
Each design has its own purposes, but with that its own set of complexities that need to be managed. These complexities can exist at both the server or the client end of the API interaction.
A product may contain a number of APIs that all fulfil different functions. Some of these APIs may be synchronous and others may be a-synchronous. Each APIs design may be independent of another,
but the logic should be consistent.

Synchronous APIs
----------------
These types of API respond to requests directly, usually providing data (or another response) immediately to requestor.

When are APIs Synchronous?
                        # This is usually the case when the data for the request is readily available. An example, when data is stored in a database or internal memory
                        # The server is able to instantly fetch the data and respond back to the client requesting the data

Benefits of a Synchronous API Design?
                        # The obvious benefit is that it allows the application to instantly receive the requested data
                        # If it is a well designed API, the application will experience better performance as everything happens quickly
                        # However, if an application requires instant data and the API is poorly designed this can introduce a bottleneck slowing everything down

Client Side Processing
                        # The application making the API request must wait for the response before performing additional code execution tasks
                        # This is why a bad API can become a bottleneck


Asynchronous APIs
-----------------
These types of APIs provide a response stating successful interaction, but do not provide any actual data. The server is required to process the request, which may take time, and then sends a notification,
or trigger that callsback to the client with the data. The client is then capable of acting on that received data.

When are APIs Asynchronous?
                        # As stated, you should expect an asynchronous API when the data request needs to be sent to another service for processing
                        # If the data is not readily available immediately it is likely going to be an Asynchronous API
                        # N.B. - this is as much because the API cannot GUARANTEE that the data will be immediately provided
                        # There is nothing that states an API that is Asynchronous cannot provide immediate data
                        # It's just not guaranteed

Benefits of an Asynchronous API Design
                        # The clear benefit is that the application can continue executing code while waiting for the Asynchronous response
                        # As a result the application may be more performant as it can multi-task & make other requests after sending the API call
                        # However, abusing this may cause negative performance as applications wait for multiple callbacks and a state of waiting with no new code available to execute may occur 

Client Side Processing
                        # This design means that the design of the API on the server side determines what happens on the client side
                        # At times the client can establish a listener(observer?) or callback mechanism to receive these notifications and process when they are received
                        # Depending on the design of the application, the client may need a queue to store the request(s) to maintain order for processing
                        # Other API designs may need the client to have a polling mechanism to check the status and progress of a given request