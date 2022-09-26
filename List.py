from nodes import Node

class List:
    
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None
    
    def append(self):
        content = input("Please define content")
        new_Node = Node(content)
        
        if self.is_empty():
            self.first = self.last =  new_Node 
        else:
            self.last.next_node = new_Node
            self.last = new_Node
            
        
    def is_empty(self):
        if self.first is None:
            return True
        else:
            return False
    
    def insert(self):
        
        original_node = self.current
        self.current = self.first
                
        while self.current.next_node != original_node:
            self.current = self.current.next_node
            
        content = input("Please define content")
        new_Node = Node(content)
        self.current.next_node = new_Node
        new_Node.next_node = original_node
    
    def remove(self):
        if self.is_empty() is not None:
            buffer = self.current
            self.current = self.current.next_node
            buffer2 = self.current.next_node
            self.current = None
            self.current = buffer
            self.current.next_node = buffer2
        else:
            print("Liste ist Leer!")
    
    def set_current_first(self):
        self.current = self.first
    
    def set_current_last(self):
        self.current = self.last
    
    def set_current_next(self):
        self.current = self.current.next_node
    
    def get_content(self):
        return self.current.content
    
    def set_content(self):
        content = input("New Content: ")
        self.current.content = content
    
    def loop(self):
        buffer = self.current
        self.current = self.first
        while self.current != self.last:
            print(self.current.content)
            self.current = self.current.next_node
        self.current = self.last
        print(self.current.content)
        self.current = buffer
    

        
newList = List()

for i in range (3):
    newList.append()

newList.set_current_first()
newList.set_current_next()
newList.set_current_next()
newList.insert()
newList.loop()
newList.remove()
newList.loop()