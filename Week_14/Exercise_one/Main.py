from Node import Node
from Stack import Stack

def main():
    try:
        node_one = Node("First Node")
        node_two = Node("Second Node")
        node_three = Node("Third Node")
        node_four = Node("Fourth Node")
        node_five = Node("Fifth Node")
        
        print(">> Create astack <<")
        my_stack = Stack(node_five)
        my_stack.print_stack()
        print(">> Push 4 modules <<")
        my_stack.push(node_four)
        my_stack.push(node_three)
        my_stack.push(node_two)
        my_stack.push(node_one)
        my_stack.print_stack()
        print(">> Pop one module <<")
        my_stack.pop()
        my_stack.print_stack()
        print(">> Pop one module <<")
        my_stack.pop()
        my_stack.print_stack()
        print(">> Adding a module with other module <<")
        node_new_one = Node("New First Node")
        node_new_two = Node("New Second Node")
        node_new_one.next = node_new_two
        my_stack.push(node_new_one)
        my_stack.print_stack()
        print(">> Emty Stack <<")
        my_stack.pop()
        my_stack.pop()
        my_stack.pop()
        my_stack.pop()
        my_stack.pop()
        my_stack.pop()
        my_stack.print_stack()
    except Exception as ex:
        print(f"Error in the main function: {ex}")

main()