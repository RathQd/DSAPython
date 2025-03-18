from queue import PriorityQueue


NOT_VISITED = 0
VISITED = 1

class MST:
    def __init__(self, no_of_nodes, edges):
        self.no_of_nodes = no_of_nodes        
        self.graph = [[] for _ in range(no_of_nodes)]
        for edge in edges:
            node1, node2, weight = edge
            self.graph[node1].append([node2, weight])
            self.graph[node2].append([node1, weight])
        self.visited_list =[NOT_VISITED for _ in range(no_of_nodes)]        
    
    def find_MST(self):
        mst_edges = []
        weight_sum_mst = 0
        pq = PriorityQueue()
        weight = 0
        start = 0        
        pq.put([weight, start])
        self.visited_list[0] = 1
        while not pq.empty():
            parent_weight, parent_node = pq.get()
            for child in self.graph[parent_node]:
                child_node, child_weight  = child                    
                if self.visited_list[child_node] == NOT_VISITED:
                    self.visited_list[child_node] = VISITED
                    pq.put([child_weight, child_node])
                    mst_edges.append([parent_node, child_node, child_weight])
                    weight_sum_mst += child_weight

        return weight_sum_mst, mst_edges

def test_set1_MST():
    edges = [
        [0,1,2],
        [0,3,6],
        [3,1,8],
        [1,2,3],
        [1,4,5],
        [4,2,7]
    ]
    no_of_nodes = 5    
    mst = MST(no_of_nodes, edges)
    min_weight_mst = mst.find_MST()
    print(min_weight_mst)    

test_set1_MST() 