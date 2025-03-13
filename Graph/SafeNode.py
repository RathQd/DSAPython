from Graph import create_sample_directed_graph1, create_sample_directed_graph2

NOT_VISITED = 0
VISITED  = 1

class SafeNode:

    def __init__(self):
        self.graphd = create_sample_directed_graph2()
        self.visited_list = [NOT_VISITED for _ in range(self.graphd.get_no_nodes()+1)]
        self.path_visit_list = [NOT_VISITED for _ in range(self.graphd.get_no_nodes()+1)]
    

    def find_safe_node_with_dfs(self, start_node, visited_list, path_visit_list):
        visited_list[start_node] = VISITED
        path_visit_list[start_node] = VISITED        
        for node in self.graphd.graph_using_list[start_node]:
            if visited_list[node[0]] == VISITED and path_visit_list[node[0]] == VISITED:
                return True                 
            if visited_list[node[0]] == NOT_VISITED:
                if self.find_safe_node_with_dfs(node[0], visited_list, path_visit_list) == True:
                    return True
        visited_list[start_node] = NOT_VISITED
        return False


g = SafeNode()
SafeNode = []
for node in range(1, g.graphd.get_no_nodes()+1):
    if g.visited_list[node] == NOT_VISITED:
        if g.find_safe_node_with_dfs(node, g.visited_list, g.path_visit_list) == False:
            SafeNode.append(node)

print(SafeNode)