from Node import Node
from Traverse import Traverse
from TreeOrder import TreeFromOrder

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

def create_BST_from_pre_and_in_order():
    b = BSTPreOrder()
    trav = Traverse()    
    pre_order = [8, 5, 1, 7, 10, 12]
    in_order = sorted(pre_order)
    treeOrder = TreeFromOrder(inorder=in_order, preorder=pre_order, postorder=[])
    b.tree = treeOrder.create_tree_with_in_and_pre_order(0, len(in_order)-1, 0, len(pre_order)-1)
    trav.dfs_traverse(b.tree)


create_BST_from_pre_and_in_order()







# create_BST_from_pre_order()        


