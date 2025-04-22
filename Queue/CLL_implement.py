class Node :
    def __init__(self,k):
        self.key = k
        self.next = None 

class MyQueue: 
    def __init__(self,C):
        self.l = [None]*C 
        self.cap = C 
        self.front = None
        self.size = 0
    def size(self):
        return self.size 
    def isEmpty(self):
        return (self.size == 0)
    def getFront(self):
        if self.size == 0:
            return None 
        else:
            return self.l[self.front]
    def getRear(self):
        if self.rear == None:
            return None 
        else:
            return self.l[(self.front + self.size - 1) % self.cap]
    def enque(self,x):
        if self.size == self.cap :
            return 
        else:
            rear = (self.front + self.size - 1) % self.cap
            rear = (rear+1) % self.cap
            self.l[rear] = x 
            self.size = self.size + 1 
    def dequeue(self):
        if self.size == 0 :
            return None 
        else:
            res = self.l[self.front] 
            self.front = (self.front + 1) % self.cap
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
    
