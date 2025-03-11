# Linear time approach ---> write yourself

# Constant time approach

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


    def InsertBegin(head,x):
        temp = Node(x)
        if head == None:
           temp.next = temp
           return temp
        else:
           temp.next = head.next  
           head.next = temp 
           head.key,temp.key = temp.key,head.key 

           return head


    
    @staticmethod
    def printCLL(head):
        if head == None:
            return
        print(head.key,end=" ")
        curr = head.next
        while curr != head:
            print(curr.key,end=" ")
            curr = curr.next

    

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = head

    x = int(input("Enter the node value : "))

    new_head = Node.InsertBegin(head,x)
    Node.printCLL(new_head)
