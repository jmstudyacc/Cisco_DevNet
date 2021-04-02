
# DevNet Fundamentals course
# Unit testing with PyTest

import pytest

def add5(v):
    my_val = v + 5
    return my_val

def tests_add5():
    r = add5(1)
    assert r == 6

    r = add5(5)
    assert r == 10

    r = add5(10.102645)
    assert r == 15.102645


# This is a trivial function to test
# However testing the result of the mathematics implemented in a function is important
# The results from a lower level function may then be replicated and used in higher level functions

# This is why it is vital to write code that leverages Unit-Testing to ensure correct outcomes
# 
# One tip for this:
# When concluding a work session, write a deliberately broken unit test as a placeholder 
# Come back to it again the next day and run a 'start of day' unit test
# The deliberately broken test will flag and jog your memory back to the thought processes the night before!

