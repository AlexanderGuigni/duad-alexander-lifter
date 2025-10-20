class DoubleEndedQueque:
    def __init__(self, head):
        self.head = head

    def get_last_node(self,node):
        last_node = node
        while last_node.next != None:
            last_node = last_node.next
        return last_node
    
    def get_last_node_with_next(self,node):
        node_before_last = node
        last_node = node.next
        while last_node != None and last_node.next != None:
            node_before_last = last_node
            last_node = node_before_last.next
            
        return node_before_last
    
    def push_left(self, node):
        last_node = self.get_last_node(node)
        last_node.next = self.head
        self.head = node

    def push_right(self, node):
        last_node_head = self.get_last_node(self.head)
        last_node_head.next = node
        

    def pop_left(self):
        if self.head != None:
            self.head = self.head.next

    def pop_right(self):
        if self.head != None:
            node_before_last_head = self.get_last_node_with_next(self.head)
            if(node_before_last_head.next != None):
                node_before_last_head.next = None
            else:
                self.head = None

    def print_stack(self):
        if self.head != None:
            node = self.head    
            count = 1
            while node != None:
                print(f"{count}. {node.data}")
                node = node.next
                count += 1
        else:
            print("The Queque is empty")