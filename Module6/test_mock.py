import pytest
from unittest import mock
from Module6.mock import add_five

@pytest.mark.parametrize("num,expected", [(3, 8), (4, 9)])
@mock.patch("Module6.mock.random_number")
def test_add_five(random_number ,num, expected):
    random_number.return_value = num
    assert add_five(num) == expected


@mock.patch("Module6.mock.dictionary")
def test_dictionary(dictionary):
    dictionary.return_value = mock.Mock(name="mock response",
                                               **{"status_code": 200, "msg": "hii"})

    assert dictionary().msg == "hii" and dictionary().status_code == 200