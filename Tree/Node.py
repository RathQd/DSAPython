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
    # root.right.right.right.right = Node(16)    
    # root.right.right.right.right.left = Node(17)    
    return root


def create_binary_tree1():
    root = Node(0)
    root.left = Node(1)
    # root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    # root.right.left = Node(5)
    # root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    # root.right.left.left = Node(11)
    # root.right.left.right = Node(12)
    # root.right.right.left = Node(13)
    # root.right.right.right = Node(14)    
    # root.right.right.right.left = Node(15)    
    # root.right.right.right.right = Node(16)    
    # root.right.right.right.right.left = Node(17)    
    return root



def create_binary_tree2():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    # root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)    
    # root.left.right.left = Node(8)
    # root.left.right.right = Node(9)
    
    return root


def create_binary_tree3_for_width():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)    
    root.left.left.left = Node(8)
    root.right.right.right = Node(9)
    return root


def create_binary_symmetric_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    root.left.left.right = Node(10)
    root.right.right.left = Node(10)
    return root

def create_binary_tree_with_child_sum_property():
    root = Node(13)
    root.left = Node(6)
    root.right = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(15)
    root.right.left = Node(2)
    root.right.right = Node(5)        
    return root

def create_binary_alphabet_tree():
    root = Node('a')
    
    root.left = Node('b')
    root.right = Node('c')
    
    root.left.left = Node('d')
    root.left.right = Node('e')
    
    root.right.left = Node('f')
    root.right.right = Node('g')        

    root.left.left.left = Node('h')
    root.left.left.right = Node('i')

    root.left.right.left = Node('j')
    root.left.right.right = Node('k')

    root.right.left.left = Node('l')
    root.right.left.right = Node('m')

    root.right.right.left = Node('n')   
    root.right.right.right = Node('o')   

    return root