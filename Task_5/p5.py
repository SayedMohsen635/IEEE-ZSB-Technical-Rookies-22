class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

# Insertion method in binary search tree
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        root = self.root
        while True:
            if val > root.info:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(val)
                    break
            elif val < root.info:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(val)
                    break
            else:
                break

# Program Test
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)