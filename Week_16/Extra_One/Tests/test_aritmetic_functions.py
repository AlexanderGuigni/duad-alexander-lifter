from Aritmetic.Main import sum_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers
import pytest

def test_sum_two_numbers_with_positive_integers():
    #Arrange
    a = 5
    b = 3
    #Act
    res = sum_two_numbers(a, b)
    #Assert
    assert res == 8

def test_sum_two_numbers_with_negative_integers():
    #Arrange
    a = -2
    b = -4
    #Act
    res = sum_two_numbers(a, b)
    #Assert
    assert res == -6

def test_sum_two_numbers_with_float_and_integer():
    #Arrange
    a = 2.5
    b = 4
    #Act
    res = sum_two_numbers(a, b)
    #Assert
    assert res == 6.5

def test_sum_two_numbers_with_non_numeric():
    #Arrange
    a = 5
    b = "3"
    #Act and Assert
    with pytest.raises(TypeError):
        sum_two_numbers(a, b)

def test_subtract_two_numbers_with_positive_integers():
    #Arrange
    a = 10
    b = 4
    #Act
    res = subtract_two_numbers(a, b)
    #Assert
    assert res == 6

def test_subtract_two_numbers_with_negative_integers():
    #Arrange
    a = -3
    b = -7
    #Act
    res = subtract_two_numbers(a, b)
    #Assert
    assert res == 4

def test_subtract_two_numbers_with_float_and_integer():
    #Arrange
    a = 5.5
    b = 2
    #Act
    res = subtract_two_numbers(a, b)
    #Assert
    assert res == 3.5

def test_subtract_two_numbers_with_non_numeric():
    #Arrange
    a = "10"
    b = 4
    #Act and Assert
    with pytest.raises(TypeError):
        subtract_two_numbers(a, b)      

def test_multiply_two_numbers_with_positive_integers():
    #Arrange
    a = 6
    b = 7
    #Act
    res = multiply_two_numbers(a, b)
    #Assert
    assert res == 42

def test_multiply_two_numbers_with_negative_integers():
    #Arrange
    a = -2
    b = -3
    #Act
    res = multiply_two_numbers(a, b)
    #Assert
    assert res == 6

def test_multiply_two_numbers_with_float_and_integer():
    #Arrange
    a = 3.5
    b = 2
    #Act
    res = multiply_two_numbers(a, b)
    #Assert
    assert res == 7.0

def test_multiply_two_numbers_with_non_numeric():
    #Arrange
    a = 6
    b = "7"
    #Act and Assert
    with pytest.raises(TypeError):
        multiply_two_numbers(a, b)

def test_divide_two_numbers_with_positive_integers():
    #Arrange
    a = 20
    b = 4
    #Act
    res = divide_two_numbers(a, b)
    #Assert
    assert res == 5.0

def test_divide_two_numbers_with_negative_integers():
    #Arrange
    a = -15
    b = -3
    #Act
    res = divide_two_numbers(a, b)
    #Assert
    assert res == 5.0

def test_divide_two_numbers_with_float_and_integer():
    #Arrange
    a = 7.5
    b = 2.5
    #Act
    res = divide_two_numbers(a, b)
    #Assert
    assert res == 3.0

def test_divide_two_numbers_with_non_numeric():
    #Arrange
    a = 20
    b = "4"
    #Act and Assert
    with pytest.raises(TypeError):
        divide_two_numbers(a, b)

def test_divide_two_numbers_by_zero():
    #Arrange
    a = 10
    b = 0
    #Act and Assert
    with pytest.raises(ZeroDivisionError):
        divide_two_numbers(a, b)
