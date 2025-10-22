
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

def bubble_sort_clean(list_to_sort):
    iterations = 0
    changes = 0
    for _ in range(0, len(list_to_sort)-1):
        for in_index in range(0, len(list_to_sort)-1):
            iterations += 1
            val_1 = list_to_sort[in_index]
            val_2 = list_to_sort[in_index + 1]
            if val_1 > val_2:
                list_to_sort[in_index] = val_2
                list_to_sort[in_index + 1] = val_1
                changes += 1
    print(f"Total iterations:{iterations}")
    print(f"Total changes:{changes}")
    return list_to_sort


def main():
    list_to_sort = [11,1,2,5,6,9,8,7,0,3,10]
    list_to_sort_2 = [11,1,2,5,6,9,8,7,0,3,10]
    print (bubble_sort_clean(list_to_sort))
    print("\n*****************************************************\n")
    print (bubble_sort(list_to_sort_2))

main()