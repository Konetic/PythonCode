
import source.my_functions as my_function

def test_add_negative_numbers():
    assert add(-3, -5) == -8

def test_add_mixed_numbers():
    assert add(10, -3) == 7

def test_divide_positive_numbers():
    assert divide(10, 2) == 5

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5

def test_divide_float_result():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_add():
    result = my_function.add(1, 2)
    assert result ==3


def test_divide():
    testResult =  my_function.divide(10, 2)
    assert testResult == 5

def test_divide_by_zero():

    #division = my_function(10, )
   division = my_function.divide(10,3 )

def test_string_concat():
    stringConcat = my_function.add("i ate ", "capital burgers today")
    assert stringConcat == "i ate capital burgers today"