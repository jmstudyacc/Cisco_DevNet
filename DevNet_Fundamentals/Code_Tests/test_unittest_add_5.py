# Unittest framework although achieving the same thing as PyTest requires a different architecture
# We need to subclass the built in TestCase class, and test by overriding its built-in methods or adding new methods
# with the name prepended by 'test_'
# Referring to the original 'Function_add_5.py' file, using the 'unittest' framework requires the following changes: 

import unittest

def add5(v):
    my_val = v + 5
    return my_val

class tests_add5(unittest.TestCase):                        # Subclassing the add5() function is achieved by creating a CLASS named 'tests_add5()' that accepts the argument 'unittest.Testcase'
    def test_add5(self):                                    # This is different to the PyTest as in PyTest we just created another function with the 'assert' keyword
        self.assertEqual(add5(1), 6)                        # Leverages 'Unittests' ASSERTEQUAL method in the same way the PyTest native 'assert' method was used
        self.assertEqual(add5(5), 10)                       # We run a test of the function with argument '5' and expect a result of '10'
        self.assertEqual(add5(10.102645), 15.102645)        

if __name__ == '__main__':                                  # Final stanza is a standard way of enabling command-line execution of the program
    unittest.main()                                         # Calls the main() function with the unittest module

