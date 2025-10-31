from BubbleSort.Main import sort_numeric_list
import pytest

def test_sort_numeric_list_with_small_list():
    #Arrange
    input_list = [3, 1, 2]
    #Act
    res = sort_numeric_list(input_list)
    #Assert
    assert res == [1, 2, 3]

def test_sort_numeric_list_with_long_list():
    #Arrange
    input_list = [73, 5, 94, 37, 84, 44, 98, 25, 66, 60, 46, 87, 9, 39, 88, 96, 99, 33, 59, 3, 62, 52, 36, 70, 6, 45, 13, 85, 18, 42, 30, 91, 32, 56, 48, 1, 100, 17, 20, 71, 21, 34, 2, 22, 50, 7, 31, 14, 63, 24, 12, 26, 43, 10, 28, 15, 35, 93, 38, 8, 49, 40, 64, 41, 55, 16, 11, 27, 89, 75, 53, 76, 47, 77, 86, 97, 67, 80, 19, 92, 65, 4, 74, 83, 29, 57, 23, 58, 72, 95, 78, 90, 61, 68, 51, 79, 69, 82, 81, 54]
    #Act
    res = sort_numeric_list(input_list)
    #Assert
    assert res == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]



def test_sort_numeric_list_with_empty_list():
    #Arrange
    input_list = []
    #Act and Assert
    with pytest.raises(ValueError):
        sort_numeric_list(input_list)
    

def test_sort_numeric_list_with_no_numeric_element_list():
    #Arrange
    input_list = [1, "b", "c"]
    #Act and Assert
    with pytest.raises(TypeError):
        sort_numeric_list(input_list)

def test_sort_numeric_list_string_parameter():
    #Arrange
    input_list = "not a list"
    #Act and Assert
    with pytest.raises(TypeError):
        sort_numeric_list(input_list)

def test_sort_numeric_list_numeric_parameter():
    #Arrange
    input_list = 5
    #Act and Assert
    with pytest.raises(TypeError):
        sort_numeric_list(input_list)

def test_sort_numeric_list_boolean_parameter():
    #Arrange
    input_list = True
    #Act and Assert
    with pytest.raises(TypeError):
        sort_numeric_list(input_list)