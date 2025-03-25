from Node import create_binary_tree

class Boundary:
    def __init__(self):
        self.tree = create_binary_tree()
        self.result = []

    def traverse_all_left_nodes(self, node):
        stack = []
        while node:
            if node.left != None:
                stack.append(node.data)
                node = node.left
            elif node.right != None:
                stack.append(node.data)
                node = node.right         
            else:
                break   
        return stack
    
    def traverse_all_right_nodes_reverse(self, node):
        stack = []
        while node:
            if node.right != None:
                stack.append(node.data)
                node = node.right                
            elif node.left != None:
                stack.append(node.data)
                node = node.left
            else:
                break
        return list(reversed(stack))
    
    def dfs_in_order_left_nodes(self, node, leafs):        
        if node == None:
            return
        if node.left == None and node.right == None:            
            leafs.append(node.data)
        self.dfs_in_order_left_nodes(node.left, leafs)
        self.dfs_in_order_left_nodes(node.right, leafs)        


def find_boundary_traverse():
    # left side nodes + leaf nodes(from left to right) + right side nodes
    b = Boundary()
    
    boudary_order = []
    left_nodes = b.traverse_all_left_nodes(b.tree)
    
    right_nodes = b.traverse_all_right_nodes_reverse(b.tree)
    
    leaf_nodes = []
    b.dfs_in_order_left_nodes(b.tree, leaf_nodes)
    
    
    for node in left_nodes:
        boudary_order.append(node)
    for node in leaf_nodes:
        boudary_order.append(node)
    for node in right_nodes:
        boudary_order.append(node)
    
    print(boudary_order)
        

find_boundary_traverse()


