from queue import Queue
from Node import create_binary_tree

class Views:
    def __init__(self):
        self.tree = create_binary_tree()        

    def vertical_order_traverse(self, root):
        q = Queue()
        q.put([root, 0, 0])
        vertical_order_dict = {}
        while not q.empty():
            l = q.qsize()                                    
            for _ in range(l):
                node, r, c = q.get()               
                if r not in vertical_order_dict.keys():
                    vertical_order_dict[r] = []
                    vertical_order_dict[r].append(node.data)
                else:
                    vertical_order_dict[r].append(node.data)

                if node.left:
                    q.put([node.left, r-1, c+1])
                if node.right:
                    q.put([node.right, r+1, c+1])                    
        return vertical_order_dict
    
    def level_order_traverse(self, root):
        q = Queue()
        q.put(root)
        level_order = []
        while not q.empty():
            l = q.qsize()
            level_nodes = []
            for _ in range(l):
                node = q.get()
                level_nodes.append(node.data)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            level_order.append(level_nodes)
        return level_order
    
    def top_view_of_tree(self, root):
        order_dict = self.vertical_order_traverse(root)
        for key in sorted(order_dict.keys()):
            print(order_dict[key][0], end = " ")            
    
    def bottom_view_of_tree(self, root):
        order_dict = self.vertical_order_traverse(root)        
        for k in sorted(order_dict.keys()):
            print(order_dict[k][-1], end = " ")
    
    def right_view_of_tree(self, root):
        level_order = self.level_order_traverse(root)
        for level in level_order:
            print(level[-1], end= " ")

    def left_view_of_tree(self, root):
        level_order = self.level_order_traverse(root)
        for level in level_order:
            print(level[0], end= " ")
    
    

def vertical_order():
    v = Views()

    print("Top View of Tree")
    v.top_view_of_tree(v.tree)

    print()
    print("Bottom View of Tree")
    v.bottom_view_of_tree(v.tree)

    print()
    print("Right View of Tree")
    v.right_view_of_tree(v.tree)

    print()
    print("Left View of Tree")
    v.left_view_of_tree(v.tree)

vertical_order()

