from Node import create_binary_tree3_for_width
from queue import Queue

class Width:
    def __init__(self):
        self.tree = create_binary_tree3_for_width()
        pass

    def find_max_width_of_tree(self, root):                
        maxWidth = 0        
        q = Queue()
        q.put([root, 1])        
        while not q.empty():
            l = q.qsize()
            level_nodes =[]
            min_index  = float('inf')
            for _ in range(l):                    
                node, num = q.get()                
                min_index = min(min_index, num)
                new_num = (num - min_index)
                if node.left != None:
                    q.put([node.left, 2*new_num])
                if node.right != None:
                    q.put([node.right, (2*new_num+1)])            
                level_nodes.append([node.data,new_num])
            maxWidth = max(maxWidth, (level_nodes[-1][1] - level_nodes[0][1])+1) 
                        
        return maxWidth

def find_max_width_of_tree():
    w = Width()
    width = w.find_max_width_of_tree(w.tree)
    print("Max Width of the binary tree is : ", width)

    

find_max_width_of_tree()


