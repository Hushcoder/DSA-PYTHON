import math
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    # My solution starts
    def length(head):
        len = 1 
        curr = head
        while curr:
            len += 1
            curr = curr.next
        return len
    
    def middleElement(head,length):
        middle = math.floor(length/2)
        curr = head
        for i in range(middle):
            curr = curr.next
            if curr.next == None:
                return curr.key
        return curr.key
    # My solution ends 

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

    lengtth = Node.length(head)
    print("Length of Linked List is: ", lengtth)
    print("Middle Element of Linked List is: ", Node.middleElement(head,lengtth))
