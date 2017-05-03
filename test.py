import unittest
from mock import MagicMock

from unittest_onerror import decorate_tests_with, on_error, on_fail


class TestBase(unittest.TestCase):
    def run_testcase(self, testcase):
        suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
        return unittest.TextTestRunner().run(suite)


class TestOnError(TestBase):
    def test(self):
        mock = MagicMock()

        class TestCase(unittest.TestCase):
            @on_error(mock)
            def test_which_errors(self):
                raise ValueError('Some unexpected error')

            @on_error(mock, reraise=False)
            def test_which_errors_no_reraise(self):
                raise ValueError('This error will not re-raise')

        result = self.run_testcase(TestCase)
        # mock was called twice
        self.assertEqual(mock.call_count, 2)
        # but error was re-raised only in 1 test
        self.assertEqual(len(result.errors), 1)


class TestOnFail(TestBase):
    def test_on_fail(self):
        mock = MagicMock()

        class TestCase(unittest.TestCase):
            @on_fail(mock)
            def test_which_fails(self):
                self.assertEqual(0, 1)

            @on_fail(mock, reraise=False)
            def test_which_fails_no_reraise(self):
                self.assertEqual(0, 1)

        result = self.run_testcase(TestCase)
        # mock was called twice
        self.assertEqual(mock.call_count, 2)
        # but error was re-raised only in 1 test
        self.assertEqual(len(result.failures), 1)


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
