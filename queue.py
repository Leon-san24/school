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


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self):
        name = input("Name: ")

        new_node = Node(name)

        if self.is_empty() == True:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            

    def dequeue(self):
        if self.is_empty() == False:
            self.head = self.head.next_node
            print("Dequeded!")
        else:
            return None

    def front(self):
        if self.is_empty() is None:
            return
        else:
            return self.head

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False





newQueue = Queue()

newQueue.enqueue()
newQueue.enqueue()
newQueue.enqueue()

print(newQueue.head.value)
newQueue.dequeue()
print(newQueue.head.value)
newQueue.dequeue()
print(newQueue.head.value)
newQueue.dequeue()


