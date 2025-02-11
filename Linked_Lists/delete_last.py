class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def deleteLast(head):
        if head == None:
            return None
        if head.next == None:
            return None
        curr = head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        return head

    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next
    

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    
    head = Node.deleteLast(head)
    Node.printlist(head)
