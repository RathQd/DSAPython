from Node import create_binary_symmetric_tree

class Symmetrical:
    
    def __init__(self):
        self.tree = create_binary_symmetric_tree()
    
    def dfs_symmetric(self, node1, node2):
        if node1 == None or node2 == None:
            return (node1 == node2)
        
        if node1.data != node2.data:
            return False
    
        return (self.dfs_symmetric(node1.left, node2.right)) and (self.dfs_symmetric(node1.right, node2.left))

    def is_symmetric(self, root):
        if self.dfs_symmetric(root.left, root.right) == False:
            return False
        else:             
            return True



def is_tree_symmetric():
    s = Symmetrical()
    result = s.is_symmetric(s.tree)
    print("Is Symmetric Tree : ", result)


is_tree_symmetric()


