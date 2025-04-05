from Node import create_binary_search_tree
class LCA:
    def __init__(self):
        self.tree = create_binary_search_tree()

    def find_lca(self, root, num1, num2):
        if not root:
            return 
        if root.data > num1 and root.data > num2:
            return self.find_lca(root.left, num1, num2)
        if root.data < num1 and root.data < num2:
            return self.find_lca(root.right, num1, num2)
        return root.data
        
def find_lcs_in_BST():
    l = LCA()         
    lca = l.find_lca(l.tree, 6, 11)
    print(lca)
    print(l.find_lca(l.tree, 10, 13))
    print(l.find_lca(l.tree, 3, 10))
    print(l.find_lca(l.tree, 7, 6))
    print(l.find_lca(l.tree, 6, 7))

find_lcs_in_BST()