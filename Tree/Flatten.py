from Node import create_binary_alphabet_tree
from Traverse import Traverse
from queue import Queue

class Flatten:
    def __init__(self):
        self.prev = None
        self.tree = create_binary_alphabet_tree()
        pass

    def flatten_tree(self, node):
        if node == None:
            return 
        self.flatten_tree(node.right)
        self.flatten_tree(node.left)
        node.right = self.prev
        node.left = None
        self.prev = node
    
    def Flatten_tree_with_queue(self, node):
        q = Queue()
        q.put(node)
        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            if not q.empty():
                node.right = q.queue[0]
            node.left = None
    
    def flatten_tree_with_morris_traverse(self, node):
        cur = node
        while cur != None:
            if cur.left != None:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
            cur = cur.right


def flatten_tree1():
    f = Flatten()
    f.flatten_tree(f.tree)
    t = Traverse()
    t.dfs_traverse(f.tree)


def flatten_tree2():
    f = Flatten()
    f.Flatten_tree_with_queue(f.tree)
    t = Traverse()
    t.dfs_traverse(f.tree)


def flatten_tree3():
    f = Flatten()
    f.flatten_tree_with_morris_traverse(f.tree)
    t = Traverse()
    t.dfs_traverse(f.tree)

# flatten_tree1()
# flatten_tree2()
flatten_tree2()


    