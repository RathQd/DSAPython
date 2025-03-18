"""
Bellman ford is usefull to detect the negative weight cycle and graph contains negative weights.
if there is edge between u->v if it follows, distace[u] + weight < distance[v]
"""


class BellmanFord:
    def __init__(self, no_of_nodes, edges, start):
        self.no_od_nodes = no_of_nodes
        self.edges = edges     
        self.start = start
        self.distance_list =[float('inf') for _ in range(self.no_od_nodes)]        
        pass
    
    def find_shortest_distance_to_all_with_bellman_ford(self):
        self.distance_list[self.start] = 0
        for _ in range(len(self.edges)-1):
            for edge in self.edges:
                node1, node2, weight = edge
                if self.distance_list[node1] + weight < self.distance_list[node2]:
                    self.distance_list[node2] = (self.distance_list[node1] + weight)
        
        # this will detect the negative weight cycle if any as all minimum distance should get covered in no_of_edge-1 iteration.
        for edge in self.edges:
            node1, node2, weight = edge
            if self.distance_list[node1] + weight < self.distance_list[node2]:
                return -1

        return self.distance_list

                    
def test_set1_shortest_path():
    edges =[
        [0,1,5],
        [1,2,-2],
        [1,5,-3],
        [2,4,3],
        [3,2,-6],
        [4,3,-2],
        [5,3,1]
    ]
    start = 1        
    no_of_nodes = 6
    b = BellmanFord(no_of_nodes, edges, start)
    print(b.find_shortest_distance_to_all_with_bellman_ford())

test_set1_shortest_path()