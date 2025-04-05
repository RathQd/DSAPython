from Node import create_binary_search_tree
class ValidateBST:
    def __init__(self):
        self.tree = create_binary_search_tree()        

    def validate_binary_search_tree(self, root, left_range, right_range):            
        if not root:
            return True
        if root.data < left_range or root.data > right_range:            
            return False        
        return self.validate_binary_search_tree(root.left, left_range, root.data) and self.validate_binary_search_tree(root.right, root.data, right_range)

def validate_BST():
    v = ValidateBST()
    print(v.validate_binary_search_tree(v.tree, float('-inf'), float('inf')))


validate_BST()

