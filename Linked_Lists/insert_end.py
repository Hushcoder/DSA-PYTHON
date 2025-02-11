class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def insertEnd(head,key):
        if head == None:
           return Node(key)
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(key)
        return head

    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next
    

if __name__ == '__main__':
    head = None
    head = Node.insertEnd(head,10)
    head = Node.insertEnd(head,20)
    head = Node.insertEnd(head,30)

    Node.printlist(head)
