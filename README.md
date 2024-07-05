# Pytest-Learning

## How to Install pytest


Pytest is available on PyPI. You can install it in a virtual environment using pip -
```

$ python -m venv venv         # create virtual environment
$ source venv/bin/activate    # activate virtual environment
(venv) $ python -m pip install pytest    # install pytest using pip

```

In Pytest, You don’t have to deal with any imports or classes to do testing. 
  - All you need to do is include a function with the "test_" prefix.
  - File name should also be start from "test_" prefix.


## Assert Keyword - 
The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.

syntax - 

      assert <boolean_expression>,<assertion_message>

  
  eg.-
  
    x = "hello"
    assert x != "hello", "x should not be 'hello'"    # if condition returns False, AssertionError is raised

  Output-
    
    Traceback (most recent call last):
    File "demo_ref_keyword_assert2.py", line 4, in <module>
        assert x != "hello", "x should not be 'hello'"
    AssertionError: x should not be 'hello'
      
here, if <boolean_expression> is true, it will not raise an error and return to the flow with success, else will raise an Assertion error with <assertion_message>.


## In Pytest, Testcases using Assert keyword - 

```

# test_with_pytest.py (file_name)

# A testcase that will pass always.
def test_always_passes(): 
    assert True    # write an expression that is expected to evaluate to True always

# A testcase that will fail always.
def test_always_fails():
    assert False    # write an expression that is expected to evaluate to False always

```

## Command to run these testcases - 

By default, pytest will run only those tests that are in or under the current directory.
So, Run it at that directory such that all test cases fall in or under that directory.

    (venv) $ pytest

After running this command, testcases files under the currentDirectory will be executed. 

### First section of the output -

The report shows:
1. The system state, including which versions of Python, pytest, and any plugins you have installed
2. The rootdir, or the directory to search under for configuration and tests
3. The number of tests the runner discovered
   
These items are presented in the first section of the output:
```

============================= test session starts =============================
platform win32 -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
rootdir: ...\effective-python-testing-with-pytest
collected 4 items

```
### Second section of the output -

The output then indicates the status of each test using a syntax similar to unittest:
1. A dot (.) means that the test passed.
2. An F means that the test has failed.
3. An E means that the test raised an unexpected exception.
The special characters are shown next to the name with the overall progress of the test suite shown on the right:
```

test_with_pytest.py .F                                                   [ 50%]
test_with_unittest.py F.                                                 [100%]

```
### Third section of the output -

For tests that fail, the report gives a detailed breakdown of the failure. In the example, the tests failed because assert False always fails:
```

================================== FAILURES ===================================
______________________________ test_always_fails ______________________________

    def test_always_fails():
>       assert False
E       assert False

test_with_pytest.py:7: AssertionError
________________________ TryTesting.test_always_fails _________________________

self = <test_with_unittest.TryTesting testMethod=test_always_fails>

    def test_always_fails(self):
>       self.assertTrue(False)
E       AssertionError: False is not true

test_with_unittest.py:10: AssertionError

```
This extra output can come in extremely handy when debugging.


### Last section of the output -

Finally, the report gives an overall status report of the test suite:
```

=========================== short test summary info ===========================
FAILED test_with_pytest.py::test_always_fails - assert False
FAILED test_with_unittest.py::TryTesting::test_always_fails - AssertionError:...

========================= 2 failed, 2 passed in 0.20s =========================

```
When compared to unittest, the pytest output is much more informative and readable.


