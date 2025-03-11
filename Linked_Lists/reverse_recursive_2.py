class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    # My solution starts
    @staticmethod
    def recursiveReverseLL(curr,prev=None):
        if curr == None:
            return prev
        next = curr.next 
        curr.next = prev 
        return Node.recursiveReverseLL(next,curr)

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
    new_head = Node.recursiveReverseLL(head)
    print("\nModified Linked List : ")
    Node.printlist(new_head) 
    
    