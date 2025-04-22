class Node:
    def __init__(self,k):
        self.left = None
        self.right = None 
        self.key = k

def SearchBST(root,key):
    if root == None:
        return False
    elif root.key == key :
        return True 
    elif root.key > key :
        return SearchBST(root.left,key)
    else:
        return SearchBST(root.right,key)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(80)
    root.right = Node(70)
    root.left.left = Node(40)
    root.left.right = Node(50)

    print(f'Answer : {SearchBST(root,50)}')
