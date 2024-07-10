import json
import pytest
from Module4.dummy import Student, print_dict

# built-in capsys fixture
def test_save_dict(capsys):
    _dict = {"a": 1, "b": 2}
    string_dict = json.dumps(_dict)
    print_dict(string_dict)
    assert capsys.readouterr().out == string_dict+"\n"

# custom fixtures

@pytest.fixture
def order():
    return []

@pytest.fixture
def append_first(order):
    order.append(1)

@pytest.fixture
def append_second(order, append_first):
    order.extend([2,3])


@pytest.fixture(autouse=True)
def append_third(order, append_second):
    order += [4]

def test_order(order):
    assert order == [1, 2, 3, 4]



# scope in fixtures

@pytest.fixture(scope="function") # by default scope (executed everytime whenenver a function is executed who is using this fixture)
def dummy_student(request):
    return Student(request.param["name"], request.param["age"])

@pytest.mark.parametrize("dummy_student,expected_age", [({"name" : "devanshee", "age" : 21 },21),
                                   ({"name" : "krishna", "age" : 17 },17)],
                                   indirect=["dummy_student"],
                                   ids=["student1", "student2"])
def test_make_dummy_students(dummy_student,expected_age):
    print(dummy_student.name)
    assert dummy_student.get_age() == expected_age


@pytest.fixture(scope="module") # module scope (executed only once for a module)
def dummy_student_module():
    return Student("devanshee", 19)

@pytest.fixture(scope="session") # session scope (executed only once for a session)
def dummy_student_session():
    return Student("devanshee", 19)


