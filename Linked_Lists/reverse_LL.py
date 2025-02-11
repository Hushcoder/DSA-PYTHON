class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    # My solution starts
    # using two pointers

    @staticmethod
    def reverseLL(head):
        if head == None:
            return None
        curr = head
        stack = []
        while curr is not None:
            stack.append(curr.key)
            curr = curr.next
        
        curr = head
        while curr is not None:
            curr.key = stack.pop()
            curr = curr.next            

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
    Node.reverseLL(head)
    print("\nModified Linked List : ")
    Node.printlist(head) 
    
    