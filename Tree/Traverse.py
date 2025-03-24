from Node import create_binary_tree
from queue import Queue

class Traverse:
    def __init__(self):
        self.tree = create_binary_tree()

    def pre_order_traverse(self, root):
        if root == None:
            return
        print(root.data)
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)

    def in_order_traverse(self, root):
        if root == None:
            return
        self.in_order_traverse(root.left)
        print(root.data)
        self.in_order_traverse(root.right)
    
    def post_order_traverse(self, root):
        if root == None:
            return
        self.post_order_traverse(root.left)
        self.post_order_traverse(root.right)
        print(root.data)
    
    def bfs_traverse(self, root):
        q = Queue()
        q.put(root)        
        while not q.empty():
            node = q.get()            
            print(node.data, end=" ")
            if node.right != None and node.left != None:
                q.put(node.left)
                q.put(node.right)         

    def dfs_traverse(self, root):        
        if root == None:
            return
        print(root.data, end=" ")
        self.dfs_traverse(root.left)
        self.dfs_traverse(root.right)

def traverse_tree():
    traverse =  Traverse()
    print("BFS Order")
    traverse.bfs_traverse(traverse.tree)
    print()
    print("DFS Order")
    traverse.dfs_traverse(traverse.tree)

traverse_tree()