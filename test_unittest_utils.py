import unittest
from mock import MagicMock

from unittest_utils import decorate_tests_with, handle_error, \
    handle_fail


class Test(unittest.TestCase):
    def run_testcase(self, testcase):
        suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
        unittest.TextTestRunner().run(suite)

    def test_handle_error(self):
        mock = MagicMock()

        class TestCase(unittest.TestCase):
            @handle_error(mock)
            def test_which_errors(self):
                raise ValueError('Some unexpected error')

        self.run_testcase(TestCase)
        mock.assert_called_once()

    def test_handle_fail(self):
        mock = MagicMock()

        class TestCase(unittest.TestCase):
            @handle_fail(mock)
            def test_which_fails(self):
                self.assertEqual(0, 1)

        self.run_testcase(TestCase)
        mock.assert_called_once()

    def test_decorate_tests_with(self):
        error_mock = MagicMock()
        fail_mock = MagicMock()

        @decorate_tests_with(handle_error(error_mock))
        @decorate_tests_with(handle_fail(fail_mock))
        class TestCase(unittest.TestCase):
            def test_which_errors(self):
                raise ValueError('Some unexpected error')

            def test_which_fails(self):
                self.assertEqual(0, 1)

        self.run_testcase(TestCase)
        error_mock.assert_called_once()
        fail_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
