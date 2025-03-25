from Node import create_binary_tree, create_binary_tree1

class Identical:
    def __init__(self):
        self.tree1 = create_binary_tree()
        self.tree2 = create_binary_tree1()

    def pre_order(self, node1, node2):
        if node1 == None and node2 == None:
            return 
        if node1.data != node2.data:
            return False        
                        
        if self.pre_order(node1.left, node2.left) == False or self.pre_order(node1.right, node2.right) == False:
            return False

    def is_tree_identical(self):        
        if self.pre_order(self.tree1, self.tree2) == None:
            return True
        else: 
            return False
        
def is_tree_identical():
    i = Identical()
    result = i.is_tree_identical()
    print("Is Both Tree Identical", result)
    
is_tree_identical()