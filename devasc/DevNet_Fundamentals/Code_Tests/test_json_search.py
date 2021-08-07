# PART 2: 'test_json_search.py'
# -------

import unittest # importing the unittest module to run the tests

from recursive_json_search import * # from the listed file import all the functions - these need to be in the same folder
from test_data import * # as above - folder positions important!!

# Now add a test class that subclasses the unittest TestCase class
# Start your method names with test_ to enable the unittest framework to auto-discover the tests

# We have 3 methods to test the search function
# 1 - Given exiting key in JSON object, see if the testing code can find the key
# 2 - Given a non-existent key in the JSON object, see if testing code confirms non-existent key
# 3 - Check if the function returns a list - it should always do this

class json_search_test(unittest.TestCase):
    """test module to test search function in `recursive_json_search.py` """

    def test_search_found(self):	#1
        """key should be found, return list should not be empty"""
        self.assertTrue([]!=json_search(key1,data))		# Returning empty list is FALSE
    def test_search_not_found(self):	#2
        """key should not be found, should return an empty list"""
        self.assertTrue([]==json_search(key2,data))		# Returning empty list is TRUE
    def test_is_a_list(self):	#3
        """Should return a list"""                           
        self.assertIsInstance(json_search(key1,data),list)		# Should return a LIST

if __name__ == '__main__':          # This enables you to turn the code from the CLI
    unittest.main()                 # Runs unittest.main() against the tests

# The unittest module has more features than the above, but this is sufficient to create a simple test unit script

"""
developer:unittest > python test_json_search.py
.F.
======================================================================
FAIL: test_search_found (__main__.json_search_test)
key should be found, return list should not be empty
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_json_search.py", line 20, in test_search_found
    self.assertTrue([]!=json_search(key1,data))         # Returning empty list is FALSE
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
"""

