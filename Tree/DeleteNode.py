from Node import create_binary_search_tree
from Traverse import Traverse
class DeleteNode:
    def __init__(self):
        self.tree = create_binary_search_tree()
    
    def delete_node(self, root, key):                
        dummy = root
        if root.data == key:
            return self.helper(root)      
        if root == None:
            return None
        while root:   
            if root.data < key:                
                if root.right and root.right.data == key:
                    root.right = self.helper(root.right)
                else:
                    root = root.right
            else:
                if root.left and root.left.data == key:
                    root.left = self.helper(root.left)
                else:
                    root = root.left
        return dummy
    
    def helper(self, node):
        if node.left == None:
            return node.right
        elif node.right == None:
            return node.left
        left_child = node.left
        extrem_left = self.find_extreme_left(node.right)        
        extrem_left.left = left_child        
        return node.right
    
    def find_extreme_left(self, node):   
        print(node.data)             
        while node.left:
            node = node.left
        return node

def delete_node_from_tree():
    d = DeleteNode()
    d.tree = d.delete_node(d.tree, 11)    
    d.tree = d.delete_node(d.tree, 5)    
    d.tree = d.delete_node(d.tree, 8)    
    trav = Traverse()
    trav.dfs_traverse(d.tree)
    print()    
    trav.dfs_traverse(d.tree)

delete_node_from_tree()



        




            

    

        
    