from Graph import create_sample_graph_for_cycle, create_sample_graph_for_component, create_sample_directed_graph2, create_sample_directed_graph1
from queue import Queue

VISITED = 1
NOT_VISITED = 0

class Cycle:
    def __init__(self):
        # self.graph =  create_sample_graph_for_cycle()
        self.graph = create_sample_graph_for_component()
        self.graphd = create_sample_directed_graph1()
        self.visited_list = [NOT_VISITED for _ in range(self.graph.get_no_nodes()+1)]
        self.visited_listd = [NOT_VISITED for _ in range(self.graphd.get_no_nodes()+1)]
        self.path_visit_list = [NOT_VISITED for _ in range(self.graphd.get_no_nodes()+1)]
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
        
            
    def detect_cycle_directed_dfs(self, start_node, visited_list, path_visit_list):
        visited_list[start_node] = VISITED
        path_visit_list[start_node] = VISITED
        for node in self.graphd.graph_using_list[start_node]:
            if visited_list[node[0]] == VISITED and path_visit_list[node[0]] == VISITED:
                return True
            if visited_list[node[0]] == NOT_VISITED:                
                if self.detect_cycle_directed_dfs(node[0], visited_list, path_visit_list) == True:
                    return True
                path_visit_list[node[0]] = NOT_VISITED
        return False
    
    def detect_cycle_directed_bfs(self, start_node, visited_list, path_visit_list):
        q = Queue()
        q.put(start_node)
        visited_list[start_node] = VISITED
        path_visit_list[start_node] = VISITED
        while not q.empty():
            element = q.get()
            for node in self.graphd.graph_using_list[element]:
                if visited_list[node[0]] == VISITED and path_visit_list[node[0]] == VISITED:
                    return True
                if visited_list[node[0]] == NOT_VISITED:
                    q.put(node[0])
                    visited_list[node[0]] = VISITED
                    path_visit_list[node[0]] = VISITED                    
            # path_visit_list[element] = NOT_VISITED
        return False




            
            








# g = Cycle()
# for node in range(1, len(g.visited_list)):
#     if g.visited_list[node] == NOT_VISITED:
#         print(g.detect_cycle_bfs([node,'x']))

# g1 = Cycle()
# for node in range(1, len(g1.visited_list)):    
#     if g1.visited_list[node] == NOT_VISITED:
#         print(g1.detect_cycle_dfs([node,'x']))


g2 = Cycle()
print(g2.detect_cycle_directed_dfs(1, g2.visited_listd, g2.path_visit_list))

g3 = Cycle()
print(g3.detect_cycle_directed_bfs(1, g3.visited_listd, g3.path_visit_list))


            





    
                             

