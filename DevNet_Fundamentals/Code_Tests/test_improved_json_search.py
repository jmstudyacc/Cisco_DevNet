
import unittest

from improved_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    """test module to test search function in `improved_json_search.py` """

    def test_search_found(self):
        """key should be found, return list should not be empty"""
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        """key should not be found, should return an empty list"""
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        """Should return a list"""
        self.assertIsInstance(json_search(key1,data),list)

if __name__ == '__main__':
    unittest.main()

"""
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
..F
======================================================================
FAIL: test_search_not_found (test_improved_json_search.json_search_test)
key should not be found, should return an empty list
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/developer/src/unittest/test_improved_json_search.py", line 15, in test_search_not_found
    self.assertTrue([]==json_search(key2,data))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
"""
# Notice above that the F appears at the 3rd position '..F' vs. '.F.' - this shows that the failure occurred on the 3rd test

"""
Hmm, looking at the test data in test_data.py, key2 = "XY&^$#*@!1234%^&" is not in the JSON object. But, we see the test result statement, key should not be found, should return an empty list. Now we know that our function returned a non-empty list for one of the keys. How is that possible?

In our test script we have three test methods with different keys to simulate the function getting called multiple times 
in an application with different inputs, allowing us catch issues such as in this scenario. 
In addition to the "key1" the test looks for the "key2" key value, which should be empty since it doesn't exist 
in the data. Well, our test asserts that the list is not empty, and that's not what we want. 
Let's try another approach.

"""