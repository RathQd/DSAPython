from Node import create_binary_tree
from queue import Queue


class MaxDepth:
    def __init__(self):
        self.tree = create_binary_tree()

    def find_max_depth_of_binary_tree_level_order(self, root):        
        q = Queue()
        q.put(root)
        cnt = 0
        all_level_nodes = []
        while not q.empty():
            level_size = q.qsize()            
            cnt += 1
            level_nodes = []            
            for _ in range(level_size):
                node = q.get()                
                if node.left != None:
                    q.put(node.left)
                if node.right != None:                    
                    q.put(node.right)
                level_nodes.append(node.data)
            all_level_nodes.append(level_nodes)
        print(all_level_nodes)
        return [len(all_level_nodes), cnt]  

    def find_max_depth_of_binary_tree_recursive(self, node):
        if node == None:
            return 0
        left_side = self.find_max_depth_of_binary_tree_recursive(node.left)
        right_side = self.find_max_depth_of_binary_tree_recursive(node.right)
        return 1 + max(left_side, right_side)    

def find_max_depth_of_binary_tree():
    max_depth = MaxDepth()
    depth1 = max_depth.find_max_depth_of_binary_tree_level_order(max_depth.tree)
    print("Max Depth of the Tree Level Order", depth1)
    depth2 = max_depth.find_max_depth_of_binary_tree_recursive(max_depth.tree)
    print("Max Depth of the Tree Recursive", depth2)

find_max_depth_of_binary_tree()