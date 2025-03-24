class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None    
        
def create_binary_tree():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)
    root.right.right.left = Node(13)
    root.right.right.right = Node(14)    
    # root.right.right.right.left = Node(15)    
    root.right.right.right.right = Node(16)    
    root.right.right.right.right.left = Node(17)    
    return root
