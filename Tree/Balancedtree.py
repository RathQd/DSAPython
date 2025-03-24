from Node import create_binary_tree

class Balanced_Tree:
    def __init__(self):
        self.tree = create_binary_tree()
        pass

    def depth_of_tree(self, node):
        if node == None:
            return 0
        left = self.depth_of_tree(node.left)
        right = self.depth_of_tree(node.right)    
        return 1 + max(left, right)

    def is_balanced_tree(self, node):
        if node == None:
            return True
                        
        left_height = self.depth_of_tree(node.left)
        right_height = self.depth_of_tree(node.right)
        
        if abs(left_height- right_height) > 1:
            return False
        
        left = self.is_balanced_tree(node.left)
        right = self.is_balanced_tree(node.right)
        if left == False or right == False:
            return False        
        return True

    def is_balanced_tree_optimized(self, node):
        if node == None:
            return 0
        left_height = self.is_balanced_tree_optimized(node.left)
        right_height = self.is_balanced_tree_optimized(node.right)
        if abs(left_height- right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)


def is_balanced_tree_test():
    b = Balanced_Tree()
    print(b.is_balanced_tree(b.tree))
    if b.is_balanced_tree_optimized(b.tree) == -1:
        return False
    else:
        return True


print(is_balanced_tree_test())



        

                
