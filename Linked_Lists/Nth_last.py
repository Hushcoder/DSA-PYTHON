class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    # My solution starts
    @staticmethod    ## methods with no self parameter are static method , for them no need of instance of class to be created when to use 
    def length(head):
        len = 0 
        curr = head
        while curr:
            len += 1
            curr = curr.next
        return len
    @staticmethod
    def nthLast(head,length,pos):
        if head == None:
            return -1
        if pos>length:
            return -1
        curr = head
        for _ in range(length-pos):
            curr = curr.next
        return curr.key
        
    # My solution ends 
    @staticmethod
    def printlist(head):
        curr = head
        while curr != None:
           print(curr.key,end=" ")
           curr = curr.next
    

if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(20)
    # node_3 = Node(30)
    # node_4 = Node(40)
    
    node_1.next = node_2
    # node_2.next = node_3
    # node_3.next = node_4
    head = node_1

    lengtth = Node.length(head)
    print("Length of Linked List is: ", lengtth)
    print(f'Nth Element from Last of Linked List is: {Node.nthLast(head,lengtth,3)}')