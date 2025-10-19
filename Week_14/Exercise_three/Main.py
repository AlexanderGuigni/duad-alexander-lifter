from Node import Node
from Tree import Tree

def main():
    try:
        root = Node("Root Node")

        node_left_one = Node("1L")
        node_right_one = Node("1R")

        node_left_two = Node("1_2L")
        node_right_two = Node("1_2R")

        node_left_tree = Node("1_3L")
        node_right_tree = Node("1_3R")

        node_left_four = Node("1_2_4L")
        node_right_four = Node("1_2_4R")

        node_left_five = Node("1_2_4_5L")
        node_right_five = Node("1_3_5R")

        root.left_node = node_left_one
        root.right_node = node_right_one

        node_right_one.left_node =  node_left_tree
        node_right_one.right_node = node_right_tree

        node_left_one.left_node = node_left_two
        node_left_one.right_node = node_right_two

        node_left_two.left_node = node_left_four
        node_left_two.right_node = node_right_four

        node_left_four.left_node = node_left_five

        node_right_tree.right_node = node_right_five

        my_tree = Tree(root)
        my_tree.print_tree()
        
    except Exception as ex:
        print(f"Error: {ex}")


main()