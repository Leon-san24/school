from queue import Queue
from queue import Node

def get_head(queue):
    head = queue.head
    return head

def counter(head):
    object_count = 0
    while head is not None:
        head = head.next_node
        object_count += 1
    print(object_count)

