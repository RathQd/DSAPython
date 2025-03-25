from Node import create_binary_tree2

class LeastCommonAncistor:

    def __init__(self):
        self.tree = create_binary_tree2()
        pass

    def lca(self, node, node1, node2):
        if node == None or node.data == node1 or node.data == node2:
            if node == None:
                return node
            else:
                return node.data      
                    
        l = self.lca(node.left, node1, node2)        
        r = self.lca(node.right, node1, node2)

        if l == None:
            return r
        elif r == None:
            return l
        else:
            return node.data

def find_lca():
    la = LeastCommonAncistor()
    print(la.lca(la.tree, 1, 3))

find_lca()