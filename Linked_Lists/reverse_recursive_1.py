class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    # My solution starts
    @staticmethod
    def recursiveReverseLL(head):
        if head == None:
            return head 
        if head.next == None:
            return head 
        rest_head = Node.recursiveReverseLL(head.next)
        rest_tail = head.next 
        rest_tail.next = head
        head.next = None
        return rest_head

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
    
    