from Node import create_binary_search_tree
class Ceil:
    def __init__(self):
        self.tree = create_binary_search_tree()
        self.ceil = -1
        pass

    def find_ceil(self, node, key, ceil):        
        if node == None:
            return
        if node.data == key:
            self.ceil = node.data
            return self.ceil
        elif node.data < key:
            self.find_ceil(node.right, key, ceil)
        else:
            self.ceil = node.data
            self.find_ceil(node.left, key, ceil)        
        return self.ceil
    
    def find_ceil_with_tree(self, node, key):
        ceil = -1
        while node:
            if node.data == key:
                ceil = node.data
                return ceil
            elif key > node.data:
                node = node.right
            else:
                ceil = node.data
                node = node.left
        return ceil
        
    
def find_ceil_of_key():
    c = Ceil()
    ceil = c.find_ceil(c.tree, 9, -1)
    ceil1 = c.find_ceil_with_tree(c.tree, 4)
    print(ceil1)


find_ceil_of_key()