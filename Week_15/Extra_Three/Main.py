
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
    try:
        if (my_list != None and my_list != []):
                for item in my_list:
                    if not isinstance(item, (int,float)):
                        raise TypeError("Error: Not all the elements of the list are numeric")
                print (bubble_sort(my_list))
        else:
            raise ValueError("Error: List is empty or null")
    except ValueError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)


def main():
    list_to_sort = [11,1,2,5,6,9,8,7,0,3,10,"10"]
    sort_numeric_list(list_to_sort)
    list_to_sort = []
    sort_numeric_list(list_to_sort)
    list_to_sort = None
    sort_numeric_list(list_to_sort)
    list_to_sort = [11,1,2,5,6,9,8,7,0,3,10.1,10.5]
    sort_numeric_list(list_to_sort)
    list_to_sort = [11,1,2,5,6,9,8,True,7,0,3,10]
    sort_numeric_list(list_to_sort)

main()