# As the name suggests, this test is to check the lego bricks fit together
# After completing your unit tests the next step is INTEGRATION testing

# An example being if your application that needs to consult a database
# INTEGRATION testing would test the values of the variables set when your functions are called
# You can use PyTest here to check!

import requests                     # Python module for making web requests

def get_config():
    return requests.get("http://localhost/get_config").content

def set_config(dbhost):
    requests.get("http://localhost/config_action?dbhost=" + dbhost)

save_dbhost = ""

def setUp():
    global save_dbhost
    save_dbhost = get_config()

def tearDown():
    global save_dbhost
    set_config(save_dbhost)

def test_setconfig():
    setUp()
    set_config("TESTVAL")
    assert get_config() == "ESTVAL"                         # PyTest native testing with the assert... code - worth noting that this will FAIL the testing due to typo
    tearDown()


# Note that the functions, setUp() and set_config() are called before the testing
# tearDown() is also called after the test to end the testing
# 
# Using unittest is similar but different - as the setUp() and tearDown() methods are provided by the TestCase class
# These can be overridden by the subclass you define 

# You should treat this testing like your Unit Testing
# Run the tests whenever you make significant changes and before you end for the day
# When you come back the next morning run your test to refresh!

# If following the Continuous Integration methodology, any errors found MUST be corrected before continuing

