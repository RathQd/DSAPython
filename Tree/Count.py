from Node import create_binary_alphabet_tree

class Count:
    def __init__(self):
        self.tree = create_binary_alphabet_tree()
        self.count = 0
        pass

    def count_number_of_nodes(self, node):
        if node == None:
            return
        self.count += 1
        self.count_number_of_nodes(node.left)
        self.count_number_of_nodes(node.right)
    

    def count_number_of_nodes_optimize(self, node):
        lh = self.find_left_height(node.left)
        rh = self.find_right_height(node.right)        
        if lh == rh:
            return (2**lh - 1)        
        return 1 + self.count_number_of_nodes_optimize(node.left) + self.count_number_of_nodes_optimize(node.right)

    def find_left_height(self, node):
        height = 1
        while node:
            node = node.left
            height += 1
        return height

    def find_right_height(self, node):
        height = 1
        while node:
            node = node.right
            height += 1
        return height
        
        
        
        
        

def find_number_of_nodes():
    c = Count()
    c.count_number_of_nodes(c.tree)
    count = c.count_number_of_nodes_optimize(c.tree)
    print(count)
    print(c.count)




find_number_of_nodes()