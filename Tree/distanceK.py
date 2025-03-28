from Node import create_binary_alphabet_tree
from queue import Queue

class DistanceK:
    def __init__(self):
        self.tree = create_binary_alphabet_tree()        
        self.parent_links = self.create_parent_links(self.tree)        

    def create_parent_links(self, node):
        parent_links_dict = {}        
        q = Queue()
        q.put(node)        
        while not q.empty():
            l = q.qsize()
            for _ in range(l):
                node = q.get()
                if node.left:
                    parent_links_dict[node.left] = node
                    q.put(node.left)
                if node.right:
                    parent_links_dict[node.right] = node
                    q.put(node.right)        
        return parent_links_dict

    def find_node(self, root, key):
        q = Queue() 
        q.put(root)
        while not q.empty():
            l = q.qsize()
            for _ in range(l):
                node = q.get()
                if node.data == key:
                    return node
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)        
        return 
    
    def find_nodes_at_distance_k(self, node, k, key):     
        node = self.find_node(node, key)
        if node == None:
            return "Key Not Found"
        cnt = -1   
        visited_dict = {}
        q = Queue()
        q.put(node)
        visited_dict[node.data] = 1
        while not q.empty():
            l = q.qsize()
            nodes_at_k_steps = []            
            for _ in range(l):                
                node = q.get()                
                nodes_at_k_steps.append(node.data)
                if node.left and node.left.data not in visited_dict.keys():
                    visited_dict[node.left.data] = 1                    
                    q.put(node.left)
                
                if node.right and node.right.data not in visited_dict.keys():
                    visited_dict[node.right.data] = 1
                    q.put(node.right)

                if node in self.parent_links.keys() and self.parent_links[node].data not in visited_dict.keys():
                    visited_dict[self.parent_links[node].data] = 1
                    q.put(self.parent_links[node])
            
            cnt += 1
            if cnt == k:
                return nodes_at_k_steps
        return nodes_at_k_steps, cnt



def node_at_distance_k():
    d = DistanceK()
    k = 2
    d.create_parent_links(d.tree)
    print(d.find_nodes_at_distance_k(d.tree, 6, 'b'))


node_at_distance_k()




