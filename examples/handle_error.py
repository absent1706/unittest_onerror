import unittest
from unittest_utils import handle_error

def my_error_handler(testcase, exception=None):
    print('Hey, test {} errored:\n{}'.format(testcase.id(), exception))


class MyTestCase(unittest.TestCase):
    @handle_error(my_error_handler)
    def test_which_errors(self):
        raise ValueError('Some unexpected error')


if __name__ == '__main__':
    unittest.main()