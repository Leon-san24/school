from selflist import *

newList = List()

newList.append(9)
newList.append(7)
newList.append(5)
#newList.append(24)
#newList.append(4)

def insertsort():
    flag = 0
    while True:
        newList.set_current_first()
        x = newList.current.content
        newList.set_current_next()
        y = newList.current.content
        if  x < y:
            break
        else:
            newList.set_current_first()
            newList.set_content(y)
            newList.set_current_next()
            newList.set_content(x)
            break
    while True:
        x = newList.current
        content = newList.current.content
        newList.set_current_next()
        y = newList.current.content
        if  content < y:
            break
        else:
            while newList.current != x:
                newList.set_current_first()
                newList.set_current_next()
                
            newList.set_content(content)
            newList.set_current_next()
            newList.set_content(y)
            break
        
newList.loop()
        
        
    
        


insertsort()