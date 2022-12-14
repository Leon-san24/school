from nodes import Node

class List:
    
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None
        
    def append(self, content):
        
        new_Node = Node(content)
        
        if self.is_empty():
            self.first = self.last =  new_Node 
        else:
            self.last.next_node = new_Node
            self.last = new_Node
    
    def append_input(self):
        content = input("Please define content: ")
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
            
        content = input("Please define content: ")
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
    
    def set_content(self,pcon):
        self.current.content = pcon
    
    def loop(self):
        buffer = self.current
        self.current = self.first
        while self.current != self.last:
            print(self.current.content)
            self.current = self.current.next_node
        self.current = self.last
        print(self.current.content)
        self.current = buffer
    
    def concat(self,pList):
        self.last.next_node = plist.first
        self.last = pList.last
    
    def search(self,pElement):
        buffer = self.current
        self.set_current_first()
        while self.current.content != pElement:
            if self.current.next_node is None:
                return False
            else:  
                self.current = self.current.next_node
        self.current = buffer
        return True
        
        
#newList = List()

#newList.append(2)
#newList.append(3)
#newList.append(5)
#newList.append(24)
#newList.append(4)


#print(newList.search(9))
