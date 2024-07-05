# Fixtures
Pytest takes a different approach. It leads you toward explicit dependency declarations that are still reusable thanks to the availability of fixtures. 

Pytest fixtures are functions that can create data, test doubles, or initialize system state for the test suite. Fixtures are functions that can return a wide range of values. Each test that depends on a fixture must explicitly accept that fixture as an argument, so dependencies are always stated up front:
```
# fixture_demo.py

import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1
```
Looking at the test function, you can immediately tell that it depends on a fixture, without needing to check the whole file for fixture definitions.

Fixtures can also make use of other fixtures, again by declaring them explicitly as dependencies. That means that, over time, your fixtures can become bulky and modular. Although the ability to insert fixtures into other fixtures provides enormous flexibility, it can also make managing dependencies more challenging as your test suite grows.

## When to Create Fixtures - 

While writing several tests that all make use of the same underlying test data, then a fixture can be used to pull the repeated data into a single function decorated with @pytest.fixture to indicate that the function is a pytest fixture.  

Imagine you’re writing a function, format_data_for_display(), to process the data returned by an API endpoint. The data represents a list of people, each with a given name, family name, and job title. The function should output a list of strings that include each person’s full name (their given_name followed by their family_name), a colon, and their title:
```
# format_data.py

def format_data_for_display(people):
    ...  # Implement this!

def format_data_for_excel(people):
    ... # Implement this!

```
In good TDD fashion, you’ll want to first write a test for it. You might write the following code for that:
```
# test_format_data.py

def test_format_data_for_display():      # first testcase
    people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

    assert format_data_for_display(people) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel():      # second testcase
    people = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

    assert format_data_for_excel(people) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""
```
Notably, both the tests have to repeat the definition of the people variable, which is quite a few lines of code.  

> If you find yourself writing several tests that all make use of the same underlying test data, then a fixture may be in your future. You can pull the repeated data into a single function decorated with @pytest.fixture to indicate that the function is a pytest fixture.  

You can use the fixture by adding the function reference as an argument to your tests.  
Note that you don’t call the fixture function. pytest takes care of that. You’ll be able to use the return value of the fixture function as the name of the fixture function:

```
# test_format_data.py

import pytest

@pytest.fixture
def example_people_data():    # fixture function which contains repeated data
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_format_data_for_display(example_people_data):    # fixture function passed as argument here
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):    # fixture function passed as argument here
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""

```
Be sure to name your fixture something specific. That way, you can quickly determine if you want to use it when writing new tests in the future!

## When to Avoid Fixtures - 
Fixtures are great for extracting data or objects that you use across multiple tests. However, they aren’t always as good for tests that require slight variations in the data. Littering your test suite with fixtures is no better than littering it with plain data or objects. It might even be worse because of the added layer of indirection.

Nevertheless, fixtures will likely be an integral part of your test suite. As your project grows in scope, the challenge of scale starts to come into the picture. One of the challenges facing any kind of tool is how it handles being used at scale, and luckily, pytest has a bunch of useful features that can help you manage the complexity that comes with growth.

## How to Use Fixtures at Scale - 
In pytest, fixtures are modular. Being modular means that fixtures can be imported, can import other modules, and they can depend on and import other fixtures. All this allows you to compose a suitable fixture abstraction for your use case.
> If you want to make a fixture available for your whole project without having to import it, a special configuration module called conftest.py will allow you to do that.

pytest looks for a conftest.py module in each directory. If you add your general-purpose fixtures to the conftest.py module, then you’ll be able to use that fixture throughout the module’s parent directory and in any subdirectories without having to import it. This is a great place to put your most widely used fixtures.

Another interesting use case for fixtures and conftest.py is in guarding access to resources. Imagine that you’ve written a test suite for code that deals with API calls. You want to ensure that the test suite doesn’t make any real network calls even if someone accidentally writes a test that does so.  
pytest provides a monkeypatch fixture to replace values and behaviors, which you can use to great effect:
```

# conftest.py

import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

```
By placing disable_network_calls() in conftest.py and adding the autouse=True option, you ensure that network calls will be disabled in every test across the suite. Any test that executes code calling requests.get() will raise a RuntimeError indicating that an unexpected network call would have occurred.
