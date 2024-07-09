import pytest
from Module1.Assert import add, function_true, print_hello_world, validate_age

# testcase using functions 

# use of assert
def test_function_true():
    assert function_true() == True

# use of capsys to test the system output and error
def test_print_hello_world(capsys):
    print_hello_world()
    output = capsys.readouterr().out
    assert output == "hello world\n"

# testcase using class 
class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3


def test_validate_age_valid_age():
    assert validate_age(4) == 4

# testcase to test raised exception
def test_validate_age_invalid_age():
    # if any ValueError exception raises with the matching message then testcase - pass else fail
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)

        


