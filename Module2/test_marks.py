import sys
import pytest

from Module1.Assert import add

@pytest.mark.skip(reason="skip it")
def test_add_num():
    assert add(1, 2) == 3

@pytest.mark.skipif(sys.version_info > (3, 9), reason="use python 3.9 or less")
def test_add():
    assert add(1,2) == 3

@pytest.mark.xfail(sys.platform == "ubuntu", reason="don't run on windows")
def test_add_list():
    assert add([3], [4]) == [3, 4]
