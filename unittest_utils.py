"""Declarative error and failure catching for Python unittest module"""

import inspect
from functools import wraps
# noinspection PyProtectedMember
from unittest.case import _ExpectedFailure, _UnexpectedSuccess, SkipTest


def decorate_tests_with(decorator):
    """
    :type decorator: callable
    """

    def decorate(cls):
        for attrname in dir(cls):
            attr = getattr(cls, attrname)
            if inspect.ismethod(attr) and attrname.startswith('test_'):
                setattr(cls, attrname, decorator(attr))
        return cls

    return decorate


def handle_error(handler, reraise=True):
    """
    Generic error handler for unittest test methods.
    :param handler: your error handler which accepts 2 params: 
                    testcase and error
    :type handler: callable
    :type reraise: bool
    """

    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            testcase = args[0]
            # All below are exceptions that should NOT be considered
            #  as test error.
            # See `unittest.TestCase.run`
            silent_errors = (KeyboardInterrupt, testcase.failureException,
                             _ExpectedFailure, _UnexpectedSuccess, SkipTest)
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if not isinstance(e, silent_errors):
                    handler(testcase, e)
                if reraise:
                    raise

        return wrapper

    return real_decorator


def handle_fail(handler, reraise=True):
    """
    Generic fail handler for unittest test methods.
    :param handler: your error handler which accepts 2 params: 
                    testcase and error
    :type handler: callable
    :type reraise: bool
    """
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            testcase = args[0]
            try:
                return func(*args, **kwargs)
            except testcase.failureException as e:
                handler(testcase, e)
            if reraise:
                raise

        return wrapper

    return real_decorator
