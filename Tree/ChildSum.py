from Node import create_binary_tree_with_child_sum_property

from Traverse import Traverse

class ChildSum:
    def __init__(self):
        self.tree = create_binary_tree_with_child_sum_property()
        
    def traverse(self):
        t = Traverse()
        t.bfs_traverse(self.tree)

    def validate_child_sum(self, node):
        left_amount = 0
        right_amount = 0
        if node == None:
            return True
        if node.left:
            left_amount = node.left.data                    
        if node.right:
            right_amount = node.right.data
        if node.left == None and node.right == None:
            return True                
        if node.data == (left_amount + right_amount):            
            return self.validate_child_sum(node.left) and self.validate_child_sum(node.right)
        else:
            return False        
        
        
    def find_child_sum_tree(self, node):
        left_amount, left = 0, 0
        right_amount, right = 0, 0        
        if node.left == None and node.right == None:
            return node.data
        if node.left:
            left_amount = node.left.data
        if node.right:
            right_amount = node.right.data     
        new_amount = left_amount + right_amount        
        if node.data < new_amount:
            if node.left:
                node.left.data = node.data
            if node.right:
                node.right.data = node.data        
        if node.left:
            left = self.find_child_sum_tree(node.left)
        if node.right:
            right = self.find_child_sum_tree(node.right)        
        node.data = left + right            
        return node.data

def child_sum_tree():
    c = ChildSum()
    c.find_child_sum_tree(c.tree)
    result = c.validate_child_sum(c.tree)
    print("Is it Child Sum : ", result)
    c.traverse()


child_sum_tree()