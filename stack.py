

class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_content(self):
        return self.value

    def set_content(self, pContent):
        self.value = pContent

    def set_next(self, pNext):
        self.next_node = pNext
        return self.next_node
    
    
class Stack:

    def __init__(self):
        self.head = None

    def push(self, value):

        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        
    def dequeue(self):
        if self.is_empty() == False:
            self.head = self.head.next_node
            print("Dequeded!")
        else:
            return None

    def top(self):
        if self.is_empty() is None:
            return
        else:
            return self.head

    def is_empty(self):
        return self.head is None


