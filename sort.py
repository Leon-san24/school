from stack import *
from random import randint

newStack = Stack()
stack2 = Stack()
stack1 = Stack()

for i in range(5):
    x = randint(1,1)
    print(x)
    newStack.push(x)
    

def sort(stack):
    while stack.top() is not None:
        if stack.top().value == 2:
            stack2.push(stack.head.value)
            stack.dequeue()
        
        elif stack.top().value == 1:
            stack1.push(stack.head.value)
            stack.dequeue()
            
    #print(stack2.head.value)
    #print(stack1.head.value)
        
def counter(head):
    object_count = 0
    while head is not None:
        head = head.next_node
        object_count += 1
    print(object_count)
    

sort(newStack)
counter(stack1.head)
