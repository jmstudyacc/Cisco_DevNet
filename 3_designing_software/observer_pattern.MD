### **Observer Pattern**
This behavioural pattern is a one-to-many pattern whereby many subscribe to notifications
from one. One send notifications out as events occur to update the many.

A real world example is close to following a playlist on a music streaming site. Instead of 
continuously checking playlist(s) for new content, you can receive a notification.
This is the natural evolution of the 'broadcast' approach of notifications. You can
selectively choose what you subscribe to.

Here you can consider the playlist to be like a Class and you, the user, to be another
Class. The User class maintained consistency by periodically polling the Playlist 
Class, but too much reliance between these two classes leads to tight coupling. This is
a tricky problem, but thankfully the Observer pattern helps address this issue.

The fundamental elements of this pattern are, OBSERVABLE or PUBLISHER and OBSERVER 
or SUBSCRIBER. Observers are notified when a state change occurs, when this happens
the notified observers contact the OBSERVABLE (the subject) and request a state update.
The publisher will be known as the subject, and the observers are the subscribers. 

The publisher does not know who the subscribers are and uses an approach similar to 
Multicast routing. The crux of the pattern is that you add a subscription mechanism
to the class from which you want to generate change notifications. The implementation
is quite simple:

- The publisher class stores a list of references to the objects that are subscribing
to the publisher
- The publisher must also store a list of methods for adding new subscribers and 
removing existing subscribers
  
A publisher in this pattern should know it has a list of observers and assume that
each observer conforms to the agreed abstraction interface. It should also implement
an attach & detach mechanism for objects interested in the state. For instance,
the PUBLISHER class would contain the observer pattern procedures and the business logic.
You can split this further and have an event propagator which queries the state holding
objects and notifies subscribers.

The coupling between the publisher and observer should be loose. This should take the form
of an abstract interface that defines the observer API. In a most simple case, it should
define an update() method, which may accept additional parameters, e.g. which part of the
state changed. 

The ConcreteObserver class models the objects that are subscribing to the publisher.
It stores the state that should be consistent with the reference publisher. It must
implement the Observers update() method for remaining synchronised with the publisher.
When a subscription is required, the ConcreteObserver object is passed to the attach()
method of the publisher class, which in turn, makes that object a part of the 
notification process

The publisher class should not be tied to the type of observer object that is registered
with the publisher. The only coupling is that the observer should implement the update()
method and the publisher provides state retrieval via the get_state() method. Again,
you could make the publisher more generic by splitting the business logic and observable logic 
into separate classes. This would create an Event Propagator for any kind of concrete publisher.

The code for observer and playlist python files is partially complete. However you should
be able to run code like this in a Python terminal and get meaningful output:

```
 from observer import User
 import playlist
 simon = User('Simon')
 tina = User('Tina')
 jazz = playlist.Jazz()
 jazz.attach(simon)
 jazz.attach(tina)
 jazz.add_track('Miles Davis - Freddie Freeloader')
 simon.play_songs()
 tina.play_songs()
```

Once a number of users & genre playlists have been created it is possible to attach
users to the playlist(s). These users are then stored in the playlist's observers list
and await any changes to the playlist's state. When a new track is added to the playlist
this accounts for a state change and the users are notified. In this case you can confirm
that by having the user play their current songs!

### Applicability of Observer Pattern
The observer pattern is likely the right tool for the job, if the job requires dynamic
state updating of some other object to an unknown number of subscribers. Typically, the
mapping of publishers & observers is achieved by storing the reference to the observers
within the publisher class. 

However, this approach may be inefficient for other deployments. This could then lead to
needing to use another data structure, like a dictionary, to store the mapping. It is also
important to remember that an observer may be subscribed to multiple publishers. Therefore,
it is recommended that in the update() method the target publisher is included in the 
signature. 

In this example the observer update is triggered when an event happens on the publisher.
This triggers a notification which occurs after a state change. An issue here is that
the approach could lead to many consecutive calls to the publisher which would
trigger many notifications leading to many consecutive state synchronisation calls. In this
case it could be better to have the application code using the publisher to trigger the 
notifications. The application could call the business logic in the publisher many times,
but would then run a single update() procedure. 

For context in the above example, a notification would not be sent out when each new track
is added. Instead, a notification would be released when a batch of tracklist additions is
completed. The final step in adding the batch of tracks would be to notify observers.

It is imperative that should a publisher object be deleted that all observers be 
informed. This needs to occur at the same time or just before the publisher object is removed.
Observers cannot hold a reference to an object that no longer exists. You should not 
delete the observer as the observer may relate to other objects and publishers. When a
'delete notification' is sent out to the observers they can clean their state and remove the
chance of a reference to nothing.

A more complex subscription system would allow subscribers to attach to specific events of
an observable. The event or part of the state that the observer is interested in would be 
passed to the attach() method. On the update() method only that event or part of the state
would be passed to the update() method. This helps stop objects receiving unnecessary updates.

This pattern is application to applications requiring the subscription like behaviour. 
It is simple to introduce new subscriber classes without changing the publisher's code. 
A big win for the observer-observable approach is that relationships can be created at 
runtime. This means you do not need to stop the program and implement each attachment. A
downside is that the publisher has no context, and the subscribers are updated in a random
order. This may not be a problem and can be flexed, but could lead to more tightly coupled
code.
