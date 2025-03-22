class Bridge:    
    def __init__(self, no_of_nodes, edges):
        self.no_of_ndoes = no_of_nodes
        self.edges = edges
        self.result = []
        self.visited_list = [0 for _ in range(self.no_of_ndoes+1)]
        self.time = [-1 for _ in range(self.no_of_ndoes+1)]
        self.low = [-1 for _ in range(self.no_of_ndoes+1)]
        self.graph = [[] for _ in range(self.no_of_ndoes+1)]
        for edge in self.edges:
            node1, node2 = edge
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    
    def dfs_tarjans_algo_for_detect_bridge(self, parent, node, time, low):                  
        for child in self.graph[node]:        
            if self.visited_list[child] == 0:
                time += 1                
                low += 1
                self.visited_list[child] = 1
                self.time[child] = time
                self.low[child] = low            
                self.dfs_tarjans_algo_for_detect_bridge(node, child, time, low)     
            
            if self.visited_list[child] == 1 and child != parent:
                if self.low[child] < self.low[node]:
                    self.low[node] = self.low[child]            
        if self.low[parent] > self.low[node]:
            self.low[parent] = self.low[node]
        if self.time[parent] < self.low[node]:
            self.result.append([parent, node])
            

            
            
                                    
                

def test_set1_find_bridge_from_graph():
    no_of_nodes = 12
    edges = [
        [1,2],
        [2,3],
        [3,4],
        [4,1],
        [4,5],
        [5,6],
        [6,7],
        [6,9],
        [7,8],
        [9,8],
        [8,10],
        [10,11],
        [10,12],
        [11,12]
    ]
    b = Bridge(no_of_nodes, edges)
    start = 1
    b.visited_list[start] = 1
    b.time[start] = 1
    b.low[start] = 1
    b.dfs_tarjans_algo_for_detect_bridge(-1, start, 1, 1)    
    print("Bridges in the Graph : ",b.result, "Which is Total", len(b.result))

test_set1_find_bridge_from_graph()