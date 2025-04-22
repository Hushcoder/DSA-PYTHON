class Node:
    def __init__(self,k):
        self.left = None
        self.right = None 
        self.key = k

def InsertBST(root,key):
    new_node = Node(key)
    if root == None:
        return new_node
    temp = None
    curr = root 
    while curr != None :
        temp = curr
        if curr.key > new_node.key :
           curr = curr.left
        else:
           curr = curr.right
    if temp.key < new_node.key :
       temp.right = new_node
    else: 
       temp.left = new_node 
    return root

def Traversal(root):
    if root != None :
        Traversal(root.left)
        print(root.key)
        Traversal(root.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)

    root = InsertBST(root,20)
    Traversal(root)

    
