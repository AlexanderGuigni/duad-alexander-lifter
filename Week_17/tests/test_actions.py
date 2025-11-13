import pytest
from datetime import date
from modules.actions import *

def test_convert_string_to_date_right_format():
    #Arrange
    my_date = "12-10-2025"
    #Action
    res = convert_string_to_date(my_date)
    #Assert
    assert(isinstance(res,date))


def test_convert_string_to_date_wrong_format():
    #Arrange
    my_date = "12/13/2025"
    #Action and Assert
    with pytest.raises(ValueError):
        convert_string_to_date(my_date)
    

def test_format_to_money_no_decimal():
    #Arrage
    amount = "750"
    #Action
    res = format_to_money(amount, "₡")
    #Assert
    assert(res == "₡750.00")

def test_format_to_money_with_decimal():
    #Arrage
    amount = "750.25"
    #Action
    res = format_to_money(amount, "₡")
    #Assert
    assert(res == "₡750.25")


def test_sort_list_of_list():
    #Arrange
    my_list = [
        [1, "Category1", "Expense", "Desc1", "100.00", "12-10-2023"],
        [2, "Category2", "Income", "Desc2", "200.00", "15-11-2023"],
        [3, "Category3", "Expense", "Desc3", "150.00", "10-09-2023"],
        [4, "Category4", "Income", "Desc4", "250.00", "15-11-2023"]
    ]
    #Action
    res = sort_list_of_list(my_list)
    #Assert
    expected = [
        [4, "Category4", "Income", "Desc4", "250.00", "15-11-2023"],
        [2, "Category2", "Income", "Desc2", "200.00", "15-11-2023"],
        [1, "Category1", "Expense", "Desc1", "100.00", "12-10-2023"],
        [3, "Category3", "Expense", "Desc3", "150.00", "10-09-2023"]
    ]
    assert(res == expected)


def test_sort_list_of_list_empty_list():
    #Arrange
    my_list = []
    #Action
    res = sort_list_of_list(my_list)
    #Assert
    expected = []
    assert(res == expected)


def test_sort_list_of_list_single_element():
    #Arrange
    my_list = [[1, "Category1", "Expense", "Desc1", "100.00", "12-10-2023"]]
    #Action
    res = sort_list_of_list(my_list)
    #Assert
    expected = [[1, "Category1", "Expense", "Desc1", "100.00", "12-10-2023"]]
    assert(res == expected)


def test_compare_dates_initial_greater():
    #Arrange
    initial_date = "15-11-2023"
    final_date = "12-10-2023"
    #Action
    res = compare_dates(initial_date, final_date)
    #Assert
    assert(res == True)


def test_compare_dates_initial_equal():
    #Arrange
    initial_date = "12-10-2023"
    final_date = "12-10-2023"
    #Action
    res = compare_dates(initial_date, final_date)
    #Assert
    assert(res == True)


def test_compare_dates_initial_less():
    #Arrange
    initial_date = "10-09-2023"
    final_date = "12-10-2023"
    #Action
    res = compare_dates(initial_date, final_date)
    #Assert
    assert(res == False)