"""
An example of cyclic dependency between app.py, db.py and init.py
"""
from init import Initialization


class DB:
    def __init__(self):
        self.DB = None

    def setupDB(self):
        print("Creating database...")
        self.DB = {}
        init = Initialization()  # db.py requires the init.py Initialization method to setup a DB
        self.DB = init.loadData(DB)
