from Graph import create_sample_graph_for_bipartite
from queue import Queue

NOT_VISITED = 0
COLOR1 = 'G'
COLOR2 = 'B'

class Bipartite():

    def __init__(self):
        self.graph =  create_sample_graph_for_bipartite()
        self.visited_list = [NOT_VISITED for _ in range(self.graph.get_no_nodes()+1)]
        self.color = [NOT_VISITED for _ in range(self.graph.get_no_nodes()+1)]
        pass

    def dfs_for_bipart(self, start_node, visited_list):
        node = start_node[0]                
        node_color = start_node[1]
        visited_list[node] = node_color        
        for n in self.graph.graph_using_list[node]:
            if visited_list[n[0]] == NOT_VISITED:
                if node_color == COLOR1:
                    new_color = COLOR2
                else:
                    new_color = COLOR1                                
                if self.dfs_for_bipart([n[0], new_color], visited_list) == False:
                    return False
            elif visited_list[n[0]] == node_color:
                return False
        return True


    def bfs_for_bipart(self, start_node, visited_list):    
        q = Queue()
        q.put(start_node)
        while not q.empty():
            element = q.get()
            node =  element[0]
            color = element[1]
            visited_list[node] = color
            for n in self.graph.graph_using_list[node]:
                if visited_list[n[0]] == NOT_VISITED:
                    if color == COLOR1:
                        new_color = COLOR2
                    else:
                        new_color = COLOR1
                    q.put([n[0], new_color])
                elif visited_list[n[0]] == color:
                    return False       
        return True                     

g = Bipartite()
# print(g.dfs_for_bipart([1,'G'], g.visited_list))
print(g.bfs_for_bipart([1,'G'], g.visited_list))

