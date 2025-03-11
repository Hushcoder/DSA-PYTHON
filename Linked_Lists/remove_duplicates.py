class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    # My solution starts
   
    @staticmethod
    def removeDuplicates(head):
        if head == None:
            return None
        curr = head
        while curr is not None and curr.next is not None:
              if curr.next.key == curr.key:
                  curr.next = curr.next.next 
              else:
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
    Node.removeDuplicates(head)
    print("\nModified Linked List : ")
    Node.printlist(head) 
    
    