import pytest
from Module4.dummy import Student

@pytest.fixture
def factory_dummy_student():

    def _make_dummy_student(name, age):
        return Student(name, age)
    
    return _make_dummy_student

def get_max_age(Students):
    max_age = 0
    max_age = max(Students, key = lambda student : student.age).age
    return max_age