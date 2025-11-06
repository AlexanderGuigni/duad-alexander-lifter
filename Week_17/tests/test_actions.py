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
    

def test_filter_by_date_with_string_dates():
    #Arrage
    movement_data = [['20', 'Pet Care', 'Expense', '₡4000.00', 'Dog grooming', '19-10-2025'],['19', 'Car', 'Expense', '₡32000.00', 'Gas', '30-10-2025']]
    intial_date = "28-10-2025"
    final_date = "31-10-2025"
    #Action
    res = filter_by_date(movement_data, intial_date, final_date)
    #Assert
    assert(res == [['19', 'Car', 'Expense', '₡32000.00', 'Gas', '30-10-2025']])


def test_filter_by_date_with_date_dates():
    #Arrage
    movement_data = [['20', 'Pet Care', 'Expense', '₡4000.00', 'Dog grooming', '19-10-2025'],['19', 'Car', 'Expense', '₡32000.00', 'Gas', '30-10-2025']]
    intial_date = datetime.strptime("28-10-2025", "%d-%m-%Y").date()
    final_date = datetime.strptime("31-10-2025", "%d-%m-%Y").date()
    #Action
    res = filter_by_date(movement_data, intial_date, final_date)
    #Assert
    assert(res == [['19', 'Car', 'Expense', '₡32000.00', 'Gas', '30-10-2025']])


def test_filter_by_date_an_empty_list():
    #Arrage
    movement_data = []
    intial_date = "28-10-2025"
    final_date = "31-10-2025"
    #Action
    res = filter_by_date(movement_data, intial_date, final_date)
    #Assert
    assert(res == [])


def test_convert_list_of_lists():
    #Arrange
    dictionary_list = [{'Id': '2', 'Category': 'Housing', 'Type': 'Expense', 'Amount': '750', 'Description': 'Rent payment', 'Date': '01-10-2025'},{'Id': '3', 'Category': 'Transportation', 'Type': 'Expense', 'Amount': '45', 'Description': 'Gas refill', 'Date': '02-10-2025'},{'Id': '4', 'Category': 'Food', 'Type': 'Expense', 'Amount': '120', 'Description': 'Grocery shopping', 'Date': '03-10-2025'}]
    #Action
    res = convert_list_of_lists(dictionary_list)
    #Assert
    assert(res == [['Id', 'Category', 'Type', 'Amount', 'Description', 'Date'],[['2', 'Housing', 'Expense', '750', 'Rent payment', '01-10-2025'], ['3', 'Transportation', 'Expense', '45', 'Gas refill', '02-10-2025'], ['4', 'Food', 'Expense', '120', 'Grocery shopping', '03-10-2025']]])


def test_convert_list_of_lists_empty_list():
    #Arrange
    dictionary_list = []
    #Action
    res = convert_list_of_lists(dictionary_list)
    #Assert
    assert(res == [[],[]])


def test_format_list_to_money():
    #Arrage
    movements = [['2', 'Housing', 'Expense', '750', 'Rent payment', '01-10-2025'], ['3', 'Transportation', 'Expense', '45', 'Gas refill', '02-10-2025'], ['4', 'Food', 'Expense', '120', 'Grocery shopping', '03-10-2025']]
    #Action
    res = format_list_to_money(movements)
    #Assert
    assert(res == [['2', 'Housing', 'Expense', '₡750.00', 'Rent payment', '01-10-2025'], ['3', 'Transportation', 'Expense', '₡45.00', 'Gas refill', '02-10-2025'], ['4', 'Food', 'Expense', '₡120.00', 'Grocery shopping', '03-10-2025']])


def test_format_list_to_money_empty_list():
    #Arrage
    movements = []
    #Action
    res = format_list_to_money(movements)
    #Assert
    assert(res == [])


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
