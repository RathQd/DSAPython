from Graph import create_sample_graph_for_component

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
        print(start_node, end="")
        for neighbor in self.graph.graph_using_list[start_node]:
            if self.visited_list[neighbor[0]] == NOT_VISITED:
                self.dfs(neighbor[0])
        pass
    
    def find_connected_component(self):
        cnt = 0
        for node in range(1, self.no_of_nodes + 1):
            if self.visited_list[node] == 0:
                cnt += 1
                print("DFS order: ", end="")
                self.dfs(start_node=node)
            print("")
        return cnt


c = Connected_Component()
components = c.find_connected_component()
print("Total Connected Components : ",components)