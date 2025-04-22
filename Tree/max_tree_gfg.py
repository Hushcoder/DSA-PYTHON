class Node:
    def __init__(self,k):
        self.left = None
        self.right = None 
        self.key = k

def MaxofTree(root):
    if root == None:
        return float('-inf')
    if root != None:
        left_max = MaxofTree(root.left)
        right_max = MaxofTree(root.right)
        return max(root.key, left_max, right_max)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(80)
    root.right = Node(70)
    root.left.left = Node(40)
    root.left.right = Node(50)

    print(f'The max element of tree passed is : {MaxofTree(root)}')
