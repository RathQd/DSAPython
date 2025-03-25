from Node import create_binary_tree
class Diameter:
    def __init__(self):
        self.tree = create_binary_tree()        

    def find_height(self, node, mx):
        if node == None:
            return 0
        left = self.find_height(node.left, mx)
        right = self.find_height(node.right, mx)
        mx[0] = max(mx[0],left+right)        
        return 1 + max(left, right)

    def find_diameter_of_tree(self, root):
        max_diameter = [0]
        self.find_height(root, max_diameter)
        return max_diameter[0]        
    
def find_diameter():
    d = Diameter()    
    diameter = d.find_diameter_of_tree(d.tree)
    print("Tree of the Diameter: ", diameter)


find_diameter()

