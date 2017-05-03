import unittest
from unittest_onerror import on_error

def my_error_handler(testcase, exception=None):
    print('Hey, test {} errored:\n{}'.format(testcase.id(), exception))


class MyTestCase(unittest.TestCase):
    @on_error(my_error_handler)
    def test_which_errors(self):
        raise ValueError('Some unexpected error')

    # error will not be re-raised => test will be "OK"
    @on_error(my_error_handler, reraise=False)
    def test_which_errors_no_reraise(self):
        raise ValueError('This error will not re-raise')


if __name__ == '__main__':
    unittest.main()