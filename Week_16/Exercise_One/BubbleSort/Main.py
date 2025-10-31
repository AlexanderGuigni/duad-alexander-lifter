
def bubble_sort(list_to_sort):
    iterations = 0
    changes = 0
    last_position = 1
    for _ in range(0, len(list_to_sort)-1):
        any_change = False
        for in_index in range(0, len(list_to_sort)-last_position):
            iterations += 1
            val_1 = list_to_sort[in_index]
            val_2 = list_to_sort[in_index + 1]
            if val_1 > val_2:
                list_to_sort[in_index] = val_2
                list_to_sort[in_index + 1] = val_1
                changes += 1
                any_change = True    
        last_position += 1
        if not any_change:
            break
    print(f"Total iterations:{iterations}")
    print(f"Total changes:{changes}")
    print
    return list_to_sort

def sort_numeric_list(my_list):
    
    if (my_list != None and my_list != []):
            for item in my_list:
                if not isinstance(item, (int,float)):
                    raise TypeError("Error: Not all the elements of the list are numeric")
            return bubble_sort(my_list)
    else:
        raise ValueError("Error: List is empty or null")