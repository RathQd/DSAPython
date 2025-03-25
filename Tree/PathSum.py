from Node import create_binary_tree

class PathSum:
    def __init__(self):
        self.tree = create_binary_tree()        

    def find_max_path_sum(self, node, mx):
        if node == None:
            return 0
        left = self.find_max_path_sum(node.left, mx)
        right = self.find_max_path_sum(node.right, mx)
        mx[0] = max(mx[0], node.data + (left+right))        
        return (node.data + max(left, right))        

def find_max_path_sum():
    p = PathSum()
    mx = [0]
    p.find_max_path_sum(p.tree, mx)
    print("Max path", mx[0])
    
find_max_path_sum()