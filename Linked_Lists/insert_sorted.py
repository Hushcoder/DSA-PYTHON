class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def sortedInsert(head,x):
        temp = Node(x)
        if x<head.key:
           print("******Condition_1 Met*********")
           temp.next = head
           return temp
        print("******Condition_2 Met*********")
        curr = head
        while curr.next != None and curr.next.key<x:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        print("******* Updated them ************")
        print(f'New Head key is {head.key}') 
        
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
    
    print("**********Entering sortedInsert**********")
    Node.sortedInsert(head,35)
    print("**********Exiting sortedInsert**********")
    print("**********printing linkedlist**********")
    Node.printlist(head)
