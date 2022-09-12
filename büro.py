from queue import Queue, Node
import time 

class Büro:
    def __init__(self):
        self.queue = Queue()
        self.front = Queue().head

    
    def enqueue(self):
        self.queue.enqueue()
        
    def process(self):
        time.sleep(2)
        self.dequeue()
    
    def dequeue(self):
        self.queue.dequeue()

newbüro = Büro()

newbüro.enqueue()
newbüro.enqueue()


#newbüro.process()