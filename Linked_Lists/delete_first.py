class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    # def deleteFirst(head):
    #     temp = head.next
    #     head.next = head.next.next
    #     return temp
    def deleteFirst(head):
        if head == None:
            return None
        else:
            return head.next

    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next
    

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    
    head = Node.deleteFirst(head)
    Node.printlist(head)
