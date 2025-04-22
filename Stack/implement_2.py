class Node:
    def __init__(self, data):
        self.key = data
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def Push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.size += 1
        return temp  # Returns new head of the stack

    def stack_size(self):
        return self.size

    def peek(self):
        if self.head is None:
            return None
        return self.head.key

    def Pop(self):
        if self.head is None:
            return None
        res = self.head.key
        self.head = self.head.next
        self.size -= 1
        return res

    def printStack(self):
        curr = self.head
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.next
        print()

if __name__ == '__main__':
    stack = MyStack()

    n = int(input("Enter no. of entries: "))
    for _ in range(n):
        val = int(input("Enter the value: "))
        stack.Push(val)  # Use Push method of stack

    print("Stack contents:")
    stack.printStack()  # Corrected call

    x = int(input("Element to push: "))
    stack.Push(x)  # Push into stack

    print("Stack after push:")
    stack.printStack()  # Corrected call
