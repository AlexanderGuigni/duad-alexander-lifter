class Tree:
    def __init__(self, node):
        self.root = node


    def print_tree(self, node = None, dash = ""):
        if node != None:
            node_to_print = node
        else: 
            node_to_print = self.root

        dash_l = dash
        dash_r = dash

        if self.root != None:
            print (f"{dash}{node_to_print.data}")

            if node_to_print.left_node != None:
                dash_l += "-"
                self.print_tree(node_to_print.left_node, dash_l)

            if node_to_print.right_node != None:
                dash_r += "-"
                self.print_tree(node_to_print.right_node,dash_r)

        else:
            print("Empty tree")
