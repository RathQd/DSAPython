from Node import create_binary_search_tree, Node
from Traverse import Traverse
class AddNodeBST:
    def __init__(self):
        self.tree = create_binary_search_tree()        

    def add_node(self, root, key):
        while root:
            if root.data > key and root.left == None:
                root.left = Node(key)
            elif root.data < key and root.right == None:
                root.right = Node(key)                
            if root.data > key:
                root = root.left
            else:
                root = root.right

def add_node_in_bst():
    a = AddNodeBST()
    a.add_node(a.tree,15)
    trav = Traverse()    
    a.add_node(a.tree,4)
    a.add_node(a.tree,1)
    a.add_node(a.tree,2)
    trav.dfs_traverse(a.tree)


add_node_in_bst()

    

    

