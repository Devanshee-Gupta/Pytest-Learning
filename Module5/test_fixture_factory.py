from Module5.fixture_factory import factory_dummy_student, get_max_age

def test_get_max_age(factory_dummy_student):
    students = [
        factory_dummy_student("devanshee", 21),
        factory_dummy_student("krishna", 19),
        factory_dummy_student("deveshi", 22)
    ]

    max_age = get_max_age(students)

    assert max_age == students[2].age