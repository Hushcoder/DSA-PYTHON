class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


    def InsertEnd(head,x):
        temp = Node(x)
        if head == None:
           temp.next = temp
           return temp
        curr = head
        while curr.next != head:
           curr = curr.next
        curr.next = temp
        temp.next = head 
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

    new_head = Node.InsertEnd(head,x)
    Node.printCLL(new_head)
