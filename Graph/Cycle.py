from Graph import create_sample_graph_for_cycle, create_sample_graph_for_component, Graph
from queue import Queue

VISITED = 1
NOT_VISITED = 0

class Cycle:
    def __init__(self):
        # self.graph =  create_sample_graph_for_cycle()
        self.graph = create_sample_graph_for_component()
        self.visited_list = [NOT_VISITED for _ in range(self.graph.get_no_nodes()+1)]
        # self.graph.display_graph_as_using_list()
    
    def detect_cycle_bfs(self, start_node):
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
        return "No Cycle"
                
    def detect_cycle_dfs(self, start_node):        
        node = start_node[0]
        parent = start_node[1]
        self.visited_list[node] = VISITED            
        for neighbor in self.graph.graph_using_list[node]:                    
            if self.visited_list[neighbor[0]] == NOT_VISITED and neighbor[0] != parent:
                if self.detect_cycle_dfs([neighbor[0], node]) == True:
                    return True
            elif neighbor[0] != parent:                
                return True
        return False
        
            
            






# g = Cycle()
# for node in range(1, len(g.visited_list)):
#     if g.visited_list[node] == NOT_VISITED:
#         print(g.detect_cycle_bfs([node,'x']))

g1 = Cycle()
for node in range(1, len(g1.visited_list)):    
    if g1.visited_list[node] == NOT_VISITED:
        print(g1.detect_cycle_dfs([node,'x']))


            





    
                             

