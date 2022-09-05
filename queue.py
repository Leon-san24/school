

class Queue:

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

        def next_node(self):
            return self.next_node

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self):

        name = input("Name: ")

        new_node = self.Node(name)

        if self.head is not None:
            self.tail = new_node
            self.Node.set_next(new_node)
        else:
            self.head = new_node

    def dequeue(self):
        self.head = None

    def front(self):
        if self.is_empty():
            return
        else:
            return self.head

    def is_empty(self):
        if self.head:
            return self.head
        else:
            print("The list is empty")
            return None

Node_1 = Queue.Node("Leon",2)

print(Node_1.value)
