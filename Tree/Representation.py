class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def dfs_traverse(self, root):
        if root == None:
            return
        self.dfs_traverse(root.left)        
        self.dfs_traverse(root.right)
        print(root.data)        
        
def create_binary_tree():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    root.dfs_traverse(root)

create_binary_tree()
