import unittest
from unittest_utils import handle_fail


def my_fail_handler(testcase, exception=None):
    print('Hey, test {} failed:\n{}'.format(testcase.id(), exception))


class MyTestCase(unittest.TestCase):
    @handle_fail(my_fail_handler)
    def test_which_fails(self):
        self.assertEqual(0, 1)


if __name__ == 'main':
    unittest.main()