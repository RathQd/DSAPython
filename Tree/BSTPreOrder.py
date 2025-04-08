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
    
    def create_BST_from_pre_order1(self, pre_order, i, upper_bound):                
        if i[0] == len(pre_order) or pre_order[i[0]] > upper_bound:
            return None
        root = Node(pre_order[i[0]])
        i[0] += 1
        root.left = self.create_BST_from_pre_order1(pre_order, i, root.data)
        root.right = self.create_BST_from_pre_order1(pre_order, i, upper_bound)
        return root
        

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

def create_BST_from_pre_and_in_order1():
    b = BSTPreOrder()
    trav = Traverse()    
    pre_order = [8, 5, 1, 7, 10, 12]
    index = [0,]
    b.tree = b.create_BST_from_pre_order1(pre_order, index, float('inf'))        
    trav.dfs_traverse(b.tree)

create_BST_from_pre_and_in_order1()
# create_BST_from_pre_order()        


