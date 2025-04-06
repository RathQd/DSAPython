from Node import Node
from Traverse import Traverse

class TreeFromOrder:
    def __init__(self, inorder, preorder, postorder):
        self.inorder =  inorder
        self.preorder = preorder     
        self.postorder = postorder
        self.inorder_dict = {}
        for node in range(0, len(self.inorder)):            
            self.inorder_dict[self.inorder[node]] = node                 

    def create_tree_with_in_and_pre_order(self, inorderL, inorderR, preorderL, preorderR):            
        if inorderL > inorderR or preorderL > preorderR:
            return None                                  
        root = Node(self.preorder[preorderL])        
        root_index = self.inorder_dict[root.data]        
        left_no_of_elements = root_index - inorderL                       
        root.left = self.create_tree_with_in_and_pre_order(inorderL, root_index-1, preorderL+1, preorderL + left_no_of_elements)        
        root.right = self.create_tree_with_in_and_pre_order(root_index+1, inorderR, preorderL + left_no_of_elements+1, preorderR)
        return root        

    def create_tree_with_in_and_post_order(self, IS, IE, PS, PE):
        if IS > IE or PS > PE:
            return None     
        root = Node(self.postorder[PE])
        root_index = self.inorder_dict[self.postorder[PE]]
        right_no_of_nodes = IE - root_index
        root.left = self.create_tree_with_in_and_post_order(IS, root_index-1,  PS,  PE - right_no_of_nodes-1)
        root.right = self.create_tree_with_in_and_post_order(root_index+1, IE, PE - right_no_of_nodes, PE-1)
        return root

def create_tree_from_orders_pre_in():
    inorder = [40, 20, 50, 10, 60, 30]
    preorder = [10, 20, 40, 50, 30, 60]
    t = TreeFromOrder(inorder= inorder, preorder= preorder, postorder = [] )
    tree = t.create_tree_with_in_and_pre_order(0, len(t.inorder)-1, 0, len(t.preorder)-1)
    trav = Traverse()
    trav.dfs_traverse(tree)


def create_tree_from_orders_post_in():
    inorder = [40, 20, 50, 10, 60, 30]
    postorder = [40, 50, 20, 60, 30, 10]
    t = TreeFromOrder(inorder=inorder, postorder=postorder, preorder=[])
    tree = t.create_tree_with_in_and_post_order(0, len(t.inorder)-1, 0, len(t.postorder)-1)
    trav = Traverse()
    trav.dfs_traverse(tree)
    

# create_tree_from_orders_pre_in()
# create_tree_from_orders_post_in()