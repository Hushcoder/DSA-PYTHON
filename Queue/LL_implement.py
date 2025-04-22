class Node :
    def __init__(self,k):
        self.key = k
        self.next = None 

class MyQueue: 
    def __init__(self):
        self.front = None 
        self.rear = None 
        self.size = 0
    def size(self):
        return self.size 
    def isEmpty(self):
        return (self.size == 0)
    def getFront(self):
        return self.front.key
    def getRear(self):
        return self.rear.key
    def enque(self,x):
        temp = Node(x)
        if self.rear == None :
            self.front = temp 
        else:
            self.rear.next = temp 
        self.rear = temp 
        self.size = self.size + 1 
    def dequeue(self):
        if self.front == None :
            return None 
        else:
            res = self.front.key 
            self.front = self.front.next 
            if self.front == None :
                self.rear = None 
            self.size = self.size - 1
            return res
        
if __name__ == '__main__':
    n = int(input("Enter no. of entries : "))

    head = None 
    tail = None

    for _ in range(n):
        k = int(input("Enter the key value: "))
        node = Node(k)
 
        if head == None :
            head = node 
            tail = node 
        else:
            tail.next = node 
            tail = node 
    
