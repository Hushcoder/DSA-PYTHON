class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(15)
    
    node_1.next = node_2
    node_2.next = node_3
    head = node_1

    Node.printlist(head)

    
