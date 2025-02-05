class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
    
    def search(head,x):
        index  = 1
        curr = head
        while curr != None:
            if curr.key == x:
                return index
            index += 1
            curr = curr.next
        return -1

if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(11)
    node_3 = Node(50)
    node_4 = Node(15)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    head = node_1

    ind = Node.search(head,15)
    print(f'Index of given key is {ind}')