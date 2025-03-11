class Node :
    def __init__(self,data):
        self.key = data
        self.prev = None 
        self.next = None 

class Dll:
    def __init__(self) :
        self.head = None
        self.size = 0
    
    @staticmethod
    def insertBegin(head,k):
        temp = Node(k)
        if head != None :
            head.prev = temp
        temp.next = head
        return temp
    
    @staticmethod 
    def printDll(head):
        curr = head
        while curr != None:
            print(curr.key,' ',end='')
            curr = curr.next 



if __name__ == '__main__' :
   
   n = int(input("Enter no. of entries : "))
   head = None
   tail = None
   for _ in range(n):
       d = int(input("Enter data value : "))
       node = Node(d)
       
       if head == None :
          head = node 
          tail = node 
       else:
          prev_con = tail
          tail.next = node
          tail = node 
          tail.prev = prev_con

   doublyll = Dll()
   k = int(input("Enter to insert : "))
   new_head = doublyll.insertBegin(head,k)
   Dll.printDll(new_head)
    
    
    
    
    