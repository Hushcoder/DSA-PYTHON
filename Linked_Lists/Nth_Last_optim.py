class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    # My solution starts
    # using two pointers

    @staticmethod
    def nthLast(head,k):
       if head == None:
           return None
       first = head
       second = head
       for _ in range(k):
           if first is None:
               return 
           first = first.next
       while first is not None:
           first = first.next
           second = second.next
       return second.key
    
    # My solution ends 
    @staticmethod
    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next
    

if __name__ == '__main__':
    
    head = None
    tail = None
    n = int(input("Enter the length of  LL : "))
    for _ in range(n):
        key = int(input("Enter the value of node : "))
        node = Node(key)
        if head == None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    print("Linked List : ")
    Node.printlist(head)
    print("\n")
    k = int(input("Enter position to find Element of LL : "))
    print("Element at position {} is : {}".format(k,Node.nthLast(head,k)))