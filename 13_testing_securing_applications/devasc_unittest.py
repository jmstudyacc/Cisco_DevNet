import unittest
import tools
from is_greater import is_greater


class TestTools(unittest.TestCase):
    def setUp(self):
        self.tools = Tools('admin')

    def test_true_when_greater(self):
        self.assertTrue(self.tools.is_greater(5, 4))

    def test_user(self):
        self.assertEqual(self.tools.user, 'admin')

    def test_false_when_equal(self):
        self.assertFalse(self.tools.is_greater(5, 5))

    def tearDown(self):
        self.tools.dispose()


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest()
