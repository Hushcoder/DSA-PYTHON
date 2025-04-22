class Node:
    def __init__(self,k):
        self.left = None
        self.right = None 
        self.key = k

def InsertBST(root,key):
    if root == None:
        return Node(key)
    elif root.key == key :
        return root  
    elif root.key > key :
        root.left = InsertBST(root.left,key)
    else:
        root.right = InsertBST(root.right,key)
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

    
