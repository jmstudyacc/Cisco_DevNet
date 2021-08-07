### **Model View Controller (MVC)**
Introduced in the 1970s, MVC is one of the most well known & heavily used architectural patterns. 
MVC played an influential role in UI frameworks and is still relevant and used today. In programming
a framework can be likened to a project. It can be extended by the programmer, but will contain a 
pre-determined set of handlers for user auth, db connection & other similarly used actions.

MVC comes at it from software components and their responsibilities. MVC splits the components into 3:

- Model
- View
- Controller 

The view component crucially enables you to test business logic without impacting the presentation of data.
A view usually maps to a controller, for instance, a user view with presentation logic for user information
will map to a user controller. This controller will handle the communication between the user view, and the
data model. 

One of the defining features of the MVC architecture is the separation of the model & view. The view 
component may be referred to as the front-end portion of software. This is due to the fact that the view
is the component that is exposed to the user. That fact is why you can expect different technologies and
skill sets for a front-end developer.

The controller and model components use different technologies, but are collectively referred to as the
'back-end'. The components are separate and as such the demands are different. You can use entirely
separate technologies to develop both, but this will require the expertise to hook the two components together.

The controller will take user input and translate this to a request for the model or for a view. It acts as 
the conduit between the user and the code itself. It receives input and interprets it against the specifications
defined in that controller. The controller may also be required to update the view when an item is or is no 
longer available in the view. 

In this case, the model maintains the state of an object in the application & implements 
the functions for this object. The model is crucial as it is involved in notifying the views & controllers 
of any changes in the internal code. A crucial feature of the model is that it needs to interpret the requests
coming from the controller. It may also be expected to engage with underlying storage technologies. 

You may question if the added complexity is worthwhile. However, you should also question if you want the view
to be responsible for two different & separate functions. You maintain a decoupling of code and purpose
by using a controller. 

Some common design patterns used in MVC:
- Observer
- Strategy
- Composite
- Factory
- Adapter

The controller and model relationship is a Strategy pattern. This suggests you take a class that has many
different related implementations & derive all the implementations into separate classes. These separate 
classes are then referred to as separate strategies. In the MVC context, a strategy could be the View class
which would need to interoperate with other strategies via the same generic interface. 

If the UI can be considered as elements like nested frames and buttons, it is likely you are using a 
structural composite design. Composite patterns are often used inside the view components of MVC. Listed 
earlier you can see that there are a number of design patterns, but usually the main patterns are:

- Observer
- Strategy
- Composite

The inclusion of separative views & models can lead to some issues. The prescient concern is how do you 
ensure that the right views & models are updated as needed. When model state changes, a change mechanism 
is needed to update the views. This mechanism is usually achieved by using the Observer pattern. This is 
very important, in this paradigm the VIEW acts as the OBSERVER to the MODEL. When the model state changes
the view will change accordingly. 

In a UML context, a model stores data or has an option to query data from a DB when requested by the view.
It will also contain a list of observers that subscribed to that model, as well as means to add and remove
observers as needed. Methods will be established to notify observers and get the new data for observers. You
want to ensure that it is quick & easy to add/remove observers to the model state.

Benefits & Downside of MVC pattern:

|Benefits|Downside|
|---|---
|Separation of concern|Increased complexity|
|Multiple views of the same model|Excessive number of change notifications|
|Flexible presentation changes|View and Controller tight coupling|
|Independent testing of components|Separate controller is sometimes not needed 
|Pluggable components| 

Implementing MVC requires that the 3 components are implemented together with connections between them.
A pivotal aspect of this approach is that the MVC components are not tighly coupled. The view must be
independent of the model and any changes in that view should not affect any other views that relate to 
the same model. The views & controllers shoudl be easily exchangeable during runtime. 

It is advisable that you construct the program at a higher level, using something like UML. 

An example would be: 

- a UserView that provides a one view
- a UserController interface
- a UserModel

The controller interface will be associated with a SimpleController class that defines create() and get() 
methods for working with user objects. The UserController will communicate with the UserModel to store user
information. The view contacts the model after the state has been changed for updates.

When writing the code, it is the responsibility of the model to define what an object 
can have and what it can do. This detail is found within the user model object. The data
that is defined on the model usually impacts how the data is stored in the underlying
database. The model is required to store the data correctly and dependent components
use the model API to access the stored data.