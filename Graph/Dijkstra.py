
"""
implemented dijkstra algo with priorityQueue

"""




from queue import PriorityQueue
from Graph import create_sample2_undirected_graph_with_weight

class Dijkstra:

    def __init__(self):
        self.graph = create_sample2_undirected_graph_with_weight()        
        self.distance_list = [float('inf') for _ in range(self.graph.get_no_nodes())]

    

    def dijkstra_shortest_path_to_all(self, start):
        pq = PriorityQueue()
        pq.put((0, start))
        self.distance_list[start] = 0
        while not pq.empty():
            old_distance, node = pq.get()                   
            for child in self.graph.graph_using_list[node]:                            
                child_node, child_distance = child
                new_distance = old_distance + child_distance
                if self.distance_list[child_node] > (new_distance):
                    self.distance_list[child_node] = new_distance                    
                    pq.put((new_distance, child_node))                    
        return self.distance_list

    def dijkstra_shortest_path_from_source_to_destination(self, start, end, parent):
        
        pq = PriorityQueue()
        pq.put([0, start])
        self.distance_list[start] = 0
        
        while not pq.empty():
            old_distance, node = pq.get()
            for child in self.graph.graph_using_list[node]:
                child_node, child_distance = child
                new_distance = child_distance + old_distance
                if self.distance_list[child_node] >  new_distance:
                    self.distance_list[child_node] = new_distance
                    parent[child_node] = node
                    pq.put([new_distance, child_node])

        n = end
        result = [end]
        while parent[n] != n:
            print(n)                           
            n = parent[n]
            result.append(n)
        return result


def test_set1():
    d = Dijkstra()

    for row in d.graph.graph_using_list:
        print(row)

    for i in range(d.graph.get_no_nodes()):
        d.distance_list = [float('inf') for _ in range(d.graph.get_no_nodes())]
        print(f"for {i} Node")
        distance_list = d.dijkstra_shortest_path_to_all(i)
        print(distance_list)


def test_set2():
    d = Dijkstra()
    parent = [i for i in range(d.graph.get_no_nodes())]
    print(d.dijkstra_shortest_path_from_source_to_destination(0, 5, parent))


# print(test_set1())
print(test_set2())
        