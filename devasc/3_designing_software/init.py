"""
An example of cyclic dependency between app.py, db.py and init.py
"""

import validator

initData = {
    'Users': [
        {'name': 'Jon', 'title': 'Manager'},
        {'name': 'Jamie', 'title': 'SRE'}
    ]
}


class Initialization:
    def __init__(self):
        self.data = initData
        self.application = validator.Validator()    # init.py requires app.py to test that the DB is setup

    def loadData(self, DB):
        print(self.data)
        DB = self.data
        validate = self.validator.runTest(DB)
        if validate:
            return DB
        else:
            raise Exception('Data not loaded')