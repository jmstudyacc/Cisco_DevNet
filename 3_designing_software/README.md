### **Abstraction**
When dealing with abstraction your goal is to provide access to an object's data, 
without providing details on how the object is implemented. This creates a contract
between clients and the class implementations. Usually these abstract classes are not
instantiated, but will have subclasses that provide the required behaviour. The subclass
is not able to be instantiated until it satisfies the methods in the Abstract class.

_For an example of this, refer to abstract_device.py_

### **Encapsulation**
OOP promotes the interaction of objects during runtime. By default, an object can access
another object's data. However, this may not be desirable and so encapsulation can be used.
A typical use case is when you want to use the methods internally but not be accessible
by methods outside the class definition. Encapsulation achieves this concealing of internal
data. In statically typed languages, you achieve this by defining data as public or private.

Dynamically typed languages are slightly different. In Python there is no option of strictly 
defining data, but a convention of prefixing the name with an underscore that marks it as
non-public data. By implementing with a double underscore, you allow name mangling to occur
which makes it more difficult to accidentally break internal method calls due to subclass
overrides of methods.

_For an example of this, refer to abstract_device.py > \_\_auditLog_

Polymorphism, when a parent class defines a method that must be implemented by the child
class that method can be considered as polymorphic. The implementation would have its own
way of presenting the solution compared to the higher-level class' proposal.

Polymorphism will be found in any instance where an object can have multiple forms. If a 
method accepts more than one type of value or parameter then it is also considered to be
polymorphic.

N.B.
* Conway's Law, n-tier Architecture
* Design Patterns: Elements of Reusable Object-Oriented Software

