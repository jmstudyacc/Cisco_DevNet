# import some module for your testing
import sys
import unittest

from is_greater import is_greater


# decorator function that is used to print a report for each individual unit test in the test program
def publish_result(test):
    def result():
        value = test()
        if value[0] == value[1]:
            result = "PASS"
        else:
            result = "FAIL"
        print(f' {test.__name__}: {result}')

    return result


@publish_result
def test_true_when_greater():
    result = [is_greater(5, 4), True]
    return result


@publish_result
def test_true_when_smaller():
    result = [is_greater(4, 5), False]
    return result


@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
def test_true_when_different():
    result = [is_greater(5, 5), False]
    return result


@publish_result
def test_true_when_equal():
    result = [is_greater(5, 5), False]
    return result


if __name__ == "__main__":
    test_true_when_greater()
    test_true_when_smaller()
    test_true_when_equal()
