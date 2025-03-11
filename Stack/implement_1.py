class Node:
    def __init__(self,data):
        self.key = data 
        self.next = None 

class MyStack:
    def __init__(self):
        self.head = None 
        self.size = 0 

    def Push(self,x):
        temp = Node(x)
        temp.next = self.head 
        self.head = temp 
        self.size = self.size + 1 

        return temp
    
    def stack_size(self):
        return self.size 
    
    def peek(self):
        if self.head is None:
            return None 
        else:
            return self.head.key 
    
    def Pop(self):
        if self.head is None:
            return None 
        res = self.head.key 
        self.head = self.head.next 
        self.size = self.size - 1
        return res 
    
    def printStack(self):
        curr = self.head 
        while curr != None : 
            print(curr.key,end=" ")
            curr = curr.next
    
if __name__ == '__main__' :
   

   head = None 
   tail = None 
   
   stack = MyStack()

   n = int(input("Enter no. of entries : "))
   for _ in range(n):
       val = int(input("Enter the value : "))
       node = Node(val)

       if head == None :
           head = node 
           tail = node 
       else:
           tail.next = node
           tail = node 
    
   stack.printStack()
   print('\n')
   x = int(input("element to push : "))
   stack.Push(x)
   print('\n')
   stack.printStack()
    
    
    
    


