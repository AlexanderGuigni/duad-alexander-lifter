class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def switch_nodes_data(node):
    main_node_data = node.data
    next_node_data = node.next.data
    node.data = next_node_data
    node.next.data = main_node_data

def get_link_list_len(linked_list):
    node = linked_list    
    count = 0
    while node != None:
        node = node.next
        count += 1
    return count

def get_node_by_index(linked_list,index):
    node = linked_list 
    counter = 0
    while counter < index:
        node = node.next
        counter += 1
    return node

def bubble_sort(linked_list):
    counter = 0
    last_position = 1
    linked_list_len = get_link_list_len(linked_list)
    for _ in range(0, linked_list_len-1):
        any_change = False
        for in_index in range(0, linked_list_len-last_position):
            counter += 1
            node = get_node_by_index(linked_list,in_index)
            val_1 = node.data
            val_2 = node.next.data
            print(f"Compared {val_1} and {val_2}")
            if val_1 > val_2:
                node.data = val_2
                node.next.data = val_1
                print(f">>Changed")
                any_change = True    
        last_position += 1
        if not any_change:
            break
    print(f"Total iterations:{counter}")
    return linked_list

def print_linked_list(head):
    if head != None:
        node = head    
        count = 1
        while node != None:
            print(f"{count}. {node.data}")
            node = node.next
            count += 1
    else:
        print("The stack is empty")

def main():
    node_1 = Node(21)
    node_2 = Node(2)
    node_3 = Node(6)
    node_4 = Node(4)
    node_5 = Node(12)
    node_6 = Node(10)
    node_7 = Node(5)
    node_8 = Node(1)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8

    print_linked_list(node_1)
    #node = get_node_by_index(node_1,0)
    #print(node.data)
    #print(get_link_list_len(node_1))
    #switch_nodes_data(node_1)
    #print_linked_list(node_1)
    print("----------------------")
    bubble_sort(node_1)
    print_linked_list(node_1)


main()