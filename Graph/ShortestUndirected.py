"""
** finding the shortest distance in undirected graph with unit weight
 from the start node using the BFS and distance_list. Simple algorithm.**

 NOTE : unit weight undirected graph here we do not required visited_list because 
 here it will never be the less distance to reach out to the same node or parents
"""



from Graph import create_sample_undirected_graph_with_weight
from queue import Queue

class ShortestUndirected:
    def __init__(self):
        self.graph = create_sample_undirected_graph_with_weight()
        self.distance_list = [float('inf') for _ in range(self.graph.get_no_nodes()+1)]                
        pass
    
    def find_shortet_distance_from_source(self, start):        
        q = Queue()
        q.put(start)                
        self.distance_list[start[0]] = start[1]
        while not q.empty():
            element = q.get()                                        
            for node in self.graph.graph_using_list[element[0]]:                    
                if self.distance_list[node[0]] > (element[1]+ node[1]):
                    self.distance_list[node[0]] = (element[1] + node[1])                                
                    q.put([node[0], self.distance_list[node[0]]])
        return self.distance_list                


def test_set1_graph():
    g = ShortestUndirected()
    print(g.find_shortet_distance_from_source([1,0]))


test_set1_graph()
    
