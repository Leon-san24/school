from __future__ import annotations
class Node:

    def __init__(self, value):
        self.value = value
        self.next_node: Node | None = Node

    def get_content(self):
        return self.value

    def set_content(self, pContent):
        self.value = pContent

    def set_next(self, pNext):
        self.next_node = pNext
        return self.next_node


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self):
        name = input("Name: ")

        new_node = Node(name)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            

    def dequeue(self):
        if self.is_empty() != True:
            self.head = Node.next_node(self.head)
            print("Dequeded!")
        else:
            return None

    def front(self):
        if self.is_empty() is None:
            return
        else:
            return self.head

    def is_empty(self):
        return self.head is None


"""
Node_1 = Node("Leon")
Node_2 = Node("Leo")
Node_3 = Node("Leonard")
Node_4 = Node("Liao")

Node_1.set_next(Node_2)
Node_2.set_next(Node_3)
Node_3.set_next(Node_4)

newQueue = Queue()
newQueue.head = Node_1
newQueue.tail = Node_4

print(newQueue.head.value)
newQueue.dequeue()
print(newQueue.head.value)
newQueue.dequeue()
print(newQueue.head.value)
newQueue.dequeue()
print(newQueue.head.value)


newQueue.enqueue()
newQueue.dequeue()
print(newQueue.head.value)


"""

