from Graph import create_sample_graph_for_cycle
from queue import Queue

VISITED = 1
NOT_VISITED = 0

class Cycle:
    def __init__(self):
        self.graph =  create_sample_graph_for_cycle()
        self.visited_list = [NOT_VISITED for _ in range(self.graph.get_no_nodes()+1)]
    
    def bfs(self, start_node):
        self.visited_list[start_node[0]] = VISITED
        q = Queue()
        q.put(start_node)
        print(start_node)
        while not q.empty():            
            element = q.get()
            current = element[0]
            parent = element[1]            
            for node in self.graph.graph_using_list[current]:                
                node = node[0]                            
                if self.visited_list[node] == VISITED and node != parent:
                    return f"Cycle Detected at {node}"
                if self.visited_list[node] == NOT_VISITED:
                    self.visited_list[node] = VISITED
                    q.put([node, current])
                
g = Cycle()
print(g.bfs([1,'x']))



            





    
                             

