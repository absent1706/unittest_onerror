import unittest

from unittest_onerror import decorate_tests_with, on_error, \
    on_fail

"""
Note about print() in handlers: 
standard Python unittest doesn't sort our output by tests,
 i.e. it will print all stuff in one place which is not cool:
  http://www.qopy.me/nyjV1d2oS1WVsIT_Dm-AxA

So we recommend you to use `nosetests` or `pytest`,
 so your output will be sorted by test like this:
  http://www.qopy.me/dY_60Yj1SSyzds7fJNyk3w
"""


def my_error_handler(testcase, exception=None):
    delimiter = '*' * 20
    print(delimiter)
    print('Hey, test {} errored:\n{}'.format(testcase.id(), exception))
    print(delimiter)


def my_fail_handler(testcase, exception=None):
    delimiter = '*' * 20
    print(delimiter)
    print('Hey, test {} failed:\n{}'.format(testcase.id(), exception))
    print(delimiter)


"""
That's how you code will be like without @decorate_tests_with
"""
class MyTestCase1(unittest.TestCase):
    @on_fail(my_fail_handler)
    @on_error(my_error_handler)
    def test_which_errors(self):
        raise ValueError('Some unexpected error')

    @on_fail(my_fail_handler)
    @on_error(my_error_handler)
    def test_which_fails(self):
        self.assertEqual(0, 1)

    @on_fail(my_fail_handler)
    @on_error(my_error_handler)
    def test_which_passes(self):
        pass


"""
With awesome @decorate_tests_with, you don't need 
to add decorators before each test!
"""
@decorate_tests_with(on_fail(my_fail_handler))
@decorate_tests_with(on_error(my_error_handler))
class MyTestCase2(unittest.TestCase):
    """
    No need of
    
    @on_fail(my_fail_handler)
    @on_error(my_error_handler)
    
    before each test method. Cool!
    """
    def test_which_errors(self):
        raise ValueError('Some unexpected error')

    def test_which_fails(self):
        self.assertEqual(0, 1)

    def test_which_passes(self):
        pass


if __name__ == '__main__':
    unittest.main()
