from collections import deque
class Node:
    def __init__(self,k):
        self.left = None
        self.right = None 
        self.key = k

ls = []
def MaxofTree(root):
    if root == None:
        return 0
    if root != None:
        MaxofTree(root.left)
        ls.append(root.key)
        MaxofTree(root.right)
    return max(ls)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(80)
    root.right = Node(70)
    root.left.left = Node(40)
    root.left.right = Node(50)

    print(f'The max element of tree passed is : {MaxofTree(root)}')
