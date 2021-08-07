"""
Modules are good to organise your code, but you need to make sure you avoid some of the below issues:

- Acyclic dependencies
- Stable dependencies
- Single responsibility

If a module is cyclic then this could lead to unexpected bugs e.g. Module A <--> Module B are cyclic in dependency.
This means a a change in Module A would affect Module B, which would affect Module A which would... and a loop begins

You should ensure that modules dependencies are acyclic to avoid this.

* Dependency Inversion
* Dependency Injection

The relationship between app.py, db.py and init.py is an example of a cyclic dependency.

You should avoid doing this by having a 'parent' module that is used by all of the 'child' modules.
Preference would be that this parent module is stable, it does not experience frequent changes.

In this case, introducing the validator module has broken the cyclic dependency

* Loose coupling
* Tight coupling

Whenever crafting a solution, you should ask yourself, did the code become less understandable by your solution? Is
it harder for other developers to read? Undisguised & Visible is better than smart and hidden.

* Cohesion

A function should execute a single thing, as per McConnell, to achieve high cohesion

instead of relying on a flag inside a function signature, it would be better to create separate functions for
the possible flags - have a function that accepts the flags, but the flags then delegate to specific functions
"""
import db


class App:
    def __init__(self):
        self.running = False
        self.database = db.DB()     # app module requires the db module to start running

    def startProgram(self):
        print('Starting the app...')
        self.database.setupDB()
        self.running = True


"""    
Commented out after the creation of validator.py
def runTest(self, DB):
        print("Checking if app is ready")
        if 'Users' in DB.keys():
            return True
        else:
            return False
"""