from M1S6.M1S6 import sum_numbers_in_list, invert_string, count_lower_upper_letters, sort_string_with_words_separated_by_dash_alphabetically, remove_composite_numbers


def test_sum_numbers_in_list_with_only_positive_values():
    # Arrange
    input_list = [4, 6, 2, 29]
    # Act
    res = sum_numbers_in_list(input_list)
    # Assert
    assert res == 41

def test_sum_numbers_in_list_with_negative_and_positive_values():
    # Arrange
    input_list = [-4, 6, -2, 29]
    # Act
    res = sum_numbers_in_list(input_list)
    # Assert
    assert res == 29

def test_sum_numbers_in_list_with_only_negative_values():
    # Arrange
    input_list = [-4, -6, -2, -29]
    # Act
    res = sum_numbers_in_list(input_list)
    # Assert
    assert res == -41   

def test_invert_string_with_normal_string():
    # Arrange
    input_string = "Hello"
    # Act
    res = invert_string(input_string)
    # Assert
    assert res == "olleH"

def test_invert_string_with_list():
    # Arrange
    input_string = ["1", "2", "3", "4", "5"]
    # Act
    res = invert_string(input_string)
    # Assert
    assert res == ["5", "4", "3", "2", "1"]

def test_invert_string_with_blank_spaces():
    # Arrange
    input_string = "  Hello   World  "
    # Act
    res = invert_string(input_string)
    # Assert
    assert res == "  dlroW   olleH  "


def test_count_lower_upper_letters_combination():
    # Arrange
    input_string = "Hello World!"
    # Act
    res = count_lower_upper_letters(input_string)
    # Assert
    assert res == "There’s 2 upper cases and 8 lower cases"


def test_count_lower_upper_letters_only_lowercase():
    # Arrange
    input_string = "hello world!"
    # Act
    res = count_lower_upper_letters(input_string)
    # Assert
    assert res == "There’s 0 upper cases and 10 lower cases"


def test_count_lower_upper_letters_only_uppercase():
    # Arrange
    input_string = "HELLO WORLD!"
    # Act
    res = count_lower_upper_letters(input_string)
    # Assert
    assert res == "There’s 10 upper cases and 0 lower cases"

def test_sort_string_with_words_separated_by_dash_alphabetically():
    # Arrange
    input_string = "python-variable-funcion-computadora-monitor"
    # Act
    res = sort_string_with_words_separated_by_dash_alphabetically(input_string)
    # Assert
    assert res == "computadora-funcion-monitor-python-variable"

def test_sort_string_with_words_separated_by_dash_alphabetically_single_word():
    # Arrange
    input_string = "python"
    # Act
    res = sort_string_with_words_separated_by_dash_alphabetically(input_string)
    # Assert
    assert res == "python"

def test_sort_string_with_words_separated_by_dash_alphabetically_empty_string():
    # Arrange
    input_string = ""
    # Act
    res = sort_string_with_words_separated_by_dash_alphabetically(input_string)
    # Assert
    assert res == ""


def test_remove_composite_numbers_with_normal_list():
    # Arrange
    input_list = [10, 15, 23, 4, 7, 9, 11, 13, 16]
    # Act
    res = remove_composite_numbers(input_list)
    # Assert
    assert res == [23, 7, 11, 13]   


def test_remove_composite_numbers_with_list_without_composite_numbers():
    # Arrange
    input_list = [2, 3, 5, 7, 11, 13, 17]
    # Act
    res = remove_composite_numbers(input_list)
    # Assert
    assert res == [2, 3, 5, 7, 11, 13, 17]

def test_remove_composite_numbers_with_list_with_only_composite_numbers():
    # Arrange
    input_list = [4, 6, 8, 9, 10, 12, 14, 15]
    # Act
    res = remove_composite_numbers(input_list)
    # Assert
    assert res == []