##### Using Two pointers ---> slow and fast ###########
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def middleElement(head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.key
    

if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)
    node_4 = Node(40)
    
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    head = node_1

    print(f'Middle Element of Linked List is {Node.middleElement(head)}')
