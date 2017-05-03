import unittest
from mock import MagicMock

from unittest_onerror import decorate_tests_with, on_error, on_fail


class TestBase(unittest.TestCase):
    def run_testcase(self, testcase):
        suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
        unittest.TextTestRunner().run(suite)


class TestOnError(TestBase):
    def test(self):
        mock = MagicMock()

        class TestCase(unittest.TestCase):
            @on_error(mock)
            def test_which_errors(self):
                raise ValueError('Some unexpected error')

        self.run_testcase(TestCase)
        mock.assert_called_once()


class TestOnFail(TestBase):
    def test_on_fail(self):
        mock = MagicMock()

        class TestCase(unittest.TestCase):
            @on_fail(mock)
            def test_which_fails(self):
                self.assertEqual(0, 1)

        self.run_testcase(TestCase)
        mock.assert_called_once()


class TestDecorateTestsWith(TestBase):
    def test(self):
        error_mock = MagicMock()
        fail_mock = MagicMock()

        @decorate_tests_with(on_error(error_mock))
        @decorate_tests_with(on_fail(fail_mock))
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
