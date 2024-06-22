
from source.functions import math_func

def test_addition():
    assert math_func.add(2 , 5) == 7
    assert math_func.add(2 ) == 6
print("testing")
test_addition()

# content of test_assert2.py
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2
# content of test_foocompare.py
class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    f1 = Foo(1)
    f2 = Foo(1)
    assert f1 == f2