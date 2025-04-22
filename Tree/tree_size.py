class Node:
    def __init__(self,k):
        self.left = None
        self.right = None 
        self.key = k

def sizeTree(root):
    if root == None:
        return 0
    else:
       ls = sizeTree(root.left)
       rs = sizeTree(root.right)
    return ls + rs + 1

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(80)
    root.right = Node(70)
    root.left.left = Node(40)
    root.left.right = Node(50)

    print(f'The size of tree passed is : {sizeTree(root)}')
