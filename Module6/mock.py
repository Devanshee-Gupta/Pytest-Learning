import random
import pytest

@pytest.fixture
def random_number():
    return random.randint(1,10)

def add_five(random_number):
    return random_number+5

def dictionary():
    return { "status_code" : 200 , "msg" : "empty"}