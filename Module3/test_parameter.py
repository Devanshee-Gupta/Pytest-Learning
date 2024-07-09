import pytest
from Module1.Assert import add

@pytest.mark.parametrize("a,b,c", [(1, 2, 3),
                                   ("a", "b", "ab")],ids=["num", "str"])
def test_add(a, b, c):
    assert add(a, b) == c