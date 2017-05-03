# Error and fail catching for Python unittest module
**For now, only Python 2 supported!**

## Error handling
Have you ever wanted to catch unittest errors?
Well, of course you can try-catch every test, 
 but it's a bit tricky taking into account that some errors should not be treated as errors:

```python
import unittest
from unittest.case import _ExpectedFailure, _UnexpectedSuccess, SkipTest

class MyTest(unittest.TestCase):
    def test_something(self):
        try:
            # your actual code
        except Exception as e:
            # these errors should NOT be treated as errors
            silent_errors = (KeyboardInterrupt, self.failureException,
                             _ExpectedFailure, _UnexpectedSuccess, SkipTest)
            if not isinstance(e, silent_errors):
                # your code that handles error
```

With this package, just write your handler and decorate tests:

```python
def my_error_handler(testcase, exception=None):
    print('Hey, test {} errored:\n{}'.format(testcase.id(), exception))


class MyTestCase(unittest.TestCase):
    @handle_error(my_error_handler)
    def test_which_errors(self):
        raise ValueError('Some unexpected error')

```

![icon](http://i.piccy.info/i9/c7168c8821f9e7023e32fd784d0e2f54/1489489664/1113/1127895/rsz_18_256.png)
See [full example](examples/handle_error.py)

## Failure handling
Unlike error handling, failures can be caught easily by rewriting `unittest.TestCase.fail` method.
But we anyway added failure handling to make your life easier:
 
```python
def my_fail_handler(testcase, exception=None):
    print('Hey, test {} failed:\n{}'.format(testcase.id(), exception))


class MyTestCase(unittest.TestCase):
    @handle_fail(my_fail_handler)
    def test_which_fails(self):
        self.assertEqual(0, 1)
```
![icon](http://i.piccy.info/i9/c7168c8821f9e7023e32fd784d0e2f54/1489489664/1113/1127895/rsz_18_256.png)
See [full example](examples/handle_fail.py)


## Real-life: decorate all tests
In real life, you have a lot of test methods, and it's tedious to add decorator before each method.
So you have quick way to decorate all test methods you want:
         
```python
@decorate_tests_with(handle_fail(my_fail_handler))
@decorate_tests_with(handle_error(my_error_handler))
class TestCase(unittest.TestCase):
    def test_one(self):
        # ...
         
    def test_two(self):
        # ...   

```                                                       

> Note about `print()` in handlers.
>
> Standard Python unittest doesn't sort our output by tests,
>  i.e. it [will print all stuff in one place which is not cool](http://www.qopy.me/nyjV1d2oS1WVsIT_Dm-AxA)
> 
> So we recommend you to use `nosetests` or `pytest`,
>  so [your output will be sorted by test](http://www.qopy.me/dY_60Yj1SSyzds7fJNyk3w)
 
![icon](http://i.piccy.info/i9/c7168c8821f9e7023e32fd784d0e2f54/1489489664/1113/1127895/rsz_18_256.png)
See [full example](examples/real_life.py)

