##### Using Two pointers ---> slow and fast ###########
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
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
    
    Node.printCLL(head)