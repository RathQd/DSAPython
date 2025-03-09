from Graph import create_sample_graph_for_component
from queue import Queue

NOT_VISITED = 0
VISITED = 1

class Connected_Component:
    
    def __init__(self):
        self.graph = create_sample_graph_for_component()
        self.no_of_nodes = self.graph.get_no_nodes()
        self.visited_list = [NOT_VISITED for _ in range(self.graph.get_no_nodes()+1)]
        pass

    def dfs(self, start_node = 1):
        self.visited_list[start_node] = VISITED
        for neighbor in self.graph.graph_using_list[start_node]:
            if self.visited_list[neighbor[0]] == NOT_VISITED:
                self.dfs(neighbor[0])
        pass

    def bfs(self, start_node):
        self.visited_list[start_node] = VISITED
        q = Queue()
        q.put([start_node,1])
        while not q.empty():
            element = q.get()[0]
            for neighbor in self.graph.graph_using_list[element]:
                if self.visited_list[neighbor[0]] == NOT_VISITED:
                    self.visited_list[neighbor[0]] = VISITED
                    q.put(neighbor)
    
    def find_connected_component_dfs(self):
        cnt = 0
        for node in range(1, self.no_of_nodes + 1):
            if self.visited_list[node] == NOT_VISITED:
                cnt += 1                
                self.dfs(start_node=node)
        return cnt

    def find_connected_component_bfs(self):
        cnt = 0
        for node in range(1, self.no_of_nodes+1):
            if self.visited_list[node] == NOT_VISITED:
                cnt += 1
                self.bfs(node)
        return cnt



c1 = Connected_Component()
components_dfs = c1.find_connected_component_dfs()
print("Total Connected Components : ",components_dfs)

c2 = Connected_Component()
components_bfs = c2.find_connected_component_bfs()
print("Total Connected Components : ",components_bfs)