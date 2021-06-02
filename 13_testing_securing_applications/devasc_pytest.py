import pytest


@pytest.fixture
def tools_lib():
    import tools

    # setup
    t = tools.Tools('admin')
    yield t     # using yield instead of return, means you pass the yielded object (generator) to the test method
    # when the test method finishes the process continues at the method that yielded the object

    # teardown
    del t


def test_true_when_greater(tools_lib):
    assert tools_lib.is_greater(5, 4)


def test_user(tools_lib):
    assert tools_lib.user == "admin"


def test_false_when_equal(tools_lib):
    assert not tools_lib.is_greater(5, 5)
