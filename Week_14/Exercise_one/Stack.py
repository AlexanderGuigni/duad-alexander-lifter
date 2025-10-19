class Stack:
    def __init__(self, head):
        self.head = head

    def get_last_node(self,node):
        last_node = node
        while last_node.next != None:
            last_node = last_node.next
        return last_node
    
    def push(self, node):
        last_node = self.get_last_node(node)
        last_node.next = self.head
        self.head = node

    def pop(self):
        if self.head != None:
            self.head = self.head.next

    def print_stack(self):
        if self.head != None:
            node = self.head    
            count = 1
            while node != None:
                print(f"{count}. {node.data}")
                node = node.next
                count += 1
        else:
            print("The stack is empty")