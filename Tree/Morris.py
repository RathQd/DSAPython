from Node import create_binary_alphabet_tree
from Traverse import Traverse

class Morris:
    def __init__(self):
        self.tree = create_binary_alphabet_tree()
        pass

    def find_morris_traverse_inorder(self, tree):
        inorder = []
        cur = tree        
        while cur != None:                
            if cur.left == None:
                inorder.append(cur.data)            
                cur = cur.right
            else:            
                prev = cur.left
                while prev.right and prev.right != cur:                
                    prev = prev.right                
                if prev.right == None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    inorder.append(cur.data)                
                    cur = cur.right                
        return inorder




def create_inorder_morris_traverse():
    m = Morris()
    inorder = m.find_morris_traverse_inorder(m.tree)
    print(inorder)
    trav = Traverse()
    trav.dfs_traverse(m.tree)


create_inorder_morris_traverse()


