"""
Reviewing our function code again, we see that ret_val is a global variable, 
meaning that its value is preserved across multiple invocations of our search function. 
If the function is called and a key is matched, a value is inserted in ret_val, 
replacing a prior result. But when the function fails to find a match, ret_val remains untouched, 
so it returns the value assigned to it by a prior call. 
This is a good example of why it's bad practice to use global variables within functions.

To resolve this issue we can add an inner function to the json_search() function. 
"""

from test_data import *

def json_search(key,input_object):
    """
    Search a key from JSON object, get nothing back if key is not found
    key : keyword to be searched, case sensitive
    input_object : JSON object to be parsed
    inner_funtion() is actually doing the job
    return a list of key:value pair
    """
    ret_val=[]
    def inner_funtion(key,input_object):
        if isinstance(input_object, dict): # Handle dict
            for k, v in input_object.items():

                if k == key:
                    temp={k:v}
                    ret_val.append(temp)

                if isinstance(v, dict):
                    inner_funtion(key,v)

                elif isinstance(v, list):
                    for item in v:

                        if not isinstance(item, (str,int)):
                            inner_funtion(key,item)

        else: # handle a list, some APIs return JSON object in a list
            for val in input_object:
                if not isinstance(val, (str,int)):
                    inner_funtion(key,val)

    inner_funtion(key,input_object)
    return ret_val

print (json_search("issueSummary",data))
print (json_search("XY&^$#*@!1234%^&",data))

"""
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
[]
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

You can run the test with:
# python -m unittest test_best_json_search

Or if you want to you can run specific tests against specific methods:
# python -m unittest test_json_search.json_search_test.test_is_a_list

Only 1 test will be run and reported against in the above scenario

"""