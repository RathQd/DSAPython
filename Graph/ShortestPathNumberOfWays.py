
from queue import PriorityQueue
class ShortestPathNumberOfWays:
    def __init__(self, no_of_nodes, edges, start, end):
        self.no_of_nodes= no_of_nodes
        self.edges= edges
        self.start= start
        self.end= end
        self.distance_list = [float('inf') for _ in range(no_of_nodes)]
        self.path = [0 for _ in range(no_of_nodes)]
        self.graph = [[] for _ in range(no_of_nodes)]

        for edge in self.edges:
            node1, node2, weight = edge
            self.graph[node1].append([node2, weight])
        

    def find_number_of_shortest_ways(self):
        pq = PriorityQueue()
        pq.put([0, self.start])
        self.distance_list[self.start] = 0
        self.path[self.start] = 1
        while not pq.empty():
            old_distance , node = pq.get()            
            for child in self.graph[node]:
                child_node, child_weight = child
                new_distance = old_distance + child_weight                                        
                if self.distance_list[child_node] > new_distance:
                    self.distance_list[child_node] = new_distance                    
                    pq.put([new_distance, child_node])        
                    self.path[child_node] = self.path[node]
                elif self.distance_list[child_node] == new_distance:
                    self.path[child_node] = self.path[child_node] + self.path[node]
        if self.path != 0:
            return self.path[self.end]
        else:
            return -1
                        
def test_set1_number_of_shortest_path():
    no_of_nodes = 7
    start = 0
    end = no_of_nodes - 1
    edges = [
        [0,6,7],
        [0,1,2],
        [1,2,3],
        [1,3,3],
        [6,3,3],
        [3,5,1],
        [6,5,1],
        [2,5,1],
        [0,4,5],
        [4,6,2]
    ]
    s = ShortestPathNumberOfWays(no_of_nodes, edges, start, end)
    paths = s.find_number_of_shortest_ways()
    print("Number of Paths: ", paths)
    pass


def test_set2_number_of_shortest_path():
    no_of_nodes = 5
    start = 0
    end = no_of_nodes - 1
    edges = [
        [0,1,2],
        [0,2,2],
        [0,3,2],
        [1,4,2],
        [2,4,2],
        [3,4,2]        
    ]
    s = ShortestPathNumberOfWays(no_of_nodes, edges, start, end)
    paths = s.find_number_of_shortest_ways()
    print("Number of Paths: ", paths)
    pass


def test_set3_number_of_shortest_path():
    no_of_nodes = 9
    start = 0
    end = no_of_nodes - 1
    edges = [
        [0,1,1],
        [0,2,2],
        [0,3,1],
        [0,4,2],
        [1,5,2],
        [2,5,1],
        [3,5,2],        
        [3,7,3],       
        [3,6,2],
        [4,6,1],              
        [5,8,1],        
        [7,8,1],        
        [6,8,1],       
    ]
    s = ShortestPathNumberOfWays(no_of_nodes, edges, start, end)
    # for row in s.graph:
    #     print(row)
    paths = s.find_number_of_shortest_ways()
    print("Number of Paths: ", paths)
    pass


test_set1_number_of_shortest_path()
test_set2_number_of_shortest_path()
test_set3_number_of_shortest_path()