class Articulation:
    def __init__(self, no_of_nodes, graph):
        self.no_of_nodes = no_of_nodes
        self.graph = graph        
        self.visited_list = [0 for _ in range(self.no_of_nodes+1)]
        self.time = [0 for _ in range(self.no_of_nodes+1)]
        self.low = [-1 for _ in range(self.no_of_nodes+1)]
        self.mark = [0 for _ in range(self.no_of_nodes+1)]
        self.result = []
    
    def dfs(self, parent, node, time, low):                
        self.visited_list[node] = 1        
        no_of_child = 0
        for child in self.graph[node]:                        
            if child == parent:
                continue
            if self.visited_list[child] == 0:                
                time += 1
                low += 1
                self.time[child] = time
                self.low[child] = low
                self.dfs(node, child, time, low)            
                no_of_child += 1
            if self.visited_list[child] == 1:
                if self.low[child] < self.low[node]:
                    self.low[node] = self.time[child]
            if self.low[child] >= self.time[node] and parent != -1:
                print(node, "mark")
                self.mark[node] = 1
            if no_of_child > 1 and parent == -1:
                self.mark[node] = 1
        if self.low[parent] > self.low[node]:
            self.low[parent]= self.low[node]           
                
    def find_articulation_point(self):        
        for node in range(self.no_of_nodes):            
            if self.visited_list[node] == 0:
                print("DFS Starts form ",node)
                self.low[node] = 1
                self.time[node] = 1
                self.dfs(-1, node, 1, 1)    

        for nodei in range(len(self.mark)):
            if self.mark[nodei] == 1:
                self.result.append(nodei)
        
        if len(self.result) == 0:
            return -1
        else:
            return self.result
        
def test_set1_find_articulation_point():
    graph = [
        [1,2,3],
        [0],
        [0,3,4,5],
        [0,2],
        [2,6],
        [2,6],
        [4,5]
    ]
    # for node in range(7):
    #     print("node", node)
    #     for child in graph[node]:
    #         print("child", child)

    no_of_nodes = 7
    a = Articulation(no_of_nodes, graph)
    result = a.find_articulation_point()
    print(result)
    pass


test_set1_find_articulation_point()