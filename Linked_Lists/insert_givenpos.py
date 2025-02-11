class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def insertPos(head,key,pos):
        temp = Node(key)
        if pos == 1:
           temp.next = head
           return temp
        curr = head
        for i in range(pos-2):
            curr = curr.next
            if curr.next == None:
                return head
        temp.next = curr.next
        curr.next = temp
        return head

    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next
    

if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)
    node_4 = Node(40)
    
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    head = node_1

    Node.insertPos(head,35,4)
    Node.printlist(head)
