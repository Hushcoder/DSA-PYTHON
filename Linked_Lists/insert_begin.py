class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def insertBegin(head,key):
        temp = Node(key)
        temp.next = head
        return temp
    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next
    

if __name__ == '__main__':
    head = None
    head = Node.insertBegin(head,10)
    head = Node.insertBegin(head,20)
    head = Node.insertBegin(head,30)

    Node.printlist(head)
