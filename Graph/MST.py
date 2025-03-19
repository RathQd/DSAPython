from queue import PriorityQueue
import DisjointSet as Ds

NOT_VISITED = 0
VISITED = 1

class MST:
    def __init__(self, no_of_nodes, edges):
        self.edges = edges
        self.no_of_nodes = no_of_nodes        
        self.graph = [[] for _ in range(no_of_nodes)]
        for edge in edges:
            node1, node2, weight = edge
            self.graph[node1].append([node2, weight])
            self.graph[node2].append([node1, weight])
        self.visited_list =[NOT_VISITED for _ in range(no_of_nodes)]        
    
    def find_MST_with_prims(self):
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
    
    def find_MST_with_krushkal(self):
        mst_sum = 0
        self.edges = sorted(self.edges, key= lambda x: x[2])        
        mst_result = []
        ds = Ds.DisjointSet(self.no_of_nodes)        
        for edge in self.edges:             
            node1, node2, weight = edge
            if ds.find_parent(node1) != ds.find_parent(node2):
                ds.union_of_node_with_size(node1, node2)
                mst_result.append([node1, node2, weight])                
                mst_sum += weight
        return (mst_sum, mst_result)
        

def test_set1_MST_prims():
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
    min_weight_mst, mst_tree = mst.find_MST_with_prims()
    print(min_weight_mst, mst_tree)    



def test_set1_MST_krushkal():
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
    min_weight_mst, mst_tree = mst.find_MST_with_krushkal()
    print(min_weight_mst, mst_tree)    


test_set1_MST_prims() 
test_set1_MST_krushkal()