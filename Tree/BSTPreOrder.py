from Node import Node
from Traverse import Traverse
class BSTPreOrder:    
    def __init__(self):
        self.tree = None
        pass

    def add_node_in_binary_search_tree(self, key):        
        if self.tree is None:
            self.tree= Node(key)   
            return         
        cur = self.tree
        while cur:
            if key > cur.data and cur.right == None:
                cur.right = Node(key)
            elif key < cur.data and cur.left == None:
                cur.left = Node(key)
            if key > cur.data:
                cur = cur.right
            else:
                cur = cur.left



def create_BST_from_pre_order():
    pre_order = [8, 5, 1, 7, 10, 12]
    b = BSTPreOrder()    
    trav = Traverse()
    
    for key in range(len(pre_order)):        
        b.add_node_in_binary_search_tree(pre_order[key])
    
    trav.dfs_traverse(b.tree)
    
create_BST_from_pre_order()        


