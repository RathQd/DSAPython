class StronglyConnected:
    def __init__(self, no_of_nodes, edges):
        self.no_of_nodes = no_of_nodes
        self.graph = [[] for _ in range(no_of_nodes)]
        for edge in edges:
            node1, node2 = edge
            self.graph[node1].append(node2)                    
        self.dfs_stack = []
        self.visited_list = [0 for _ in range(no_of_nodes)]

    def dfs(self, node, reversed = False):
        if not reversed:
            for child in self.graph[node]:
                if self.visited_list[child] == 0:
                    self.visited_list[child] = 1                
                    self.dfs(child)
        else:
            for child in self.reversed_graph[node]:
                if self.visited_list[child] == 0:
                    self.visited_list[child] = 1                
                    self.dfs(child, True)
        
        if not reversed:
            self.dfs_stack.append(node)

    def find_strongly_connected_components(self, start):
        self.dfs(start)
        self.visited_list = [0 for _ in range(self.no_of_nodes)]
        self.reversed_graph = [[] for _ in range(self.no_of_nodes)]
        
        for i in range(len(self.graph)):
            for node in self.graph[i]:
                self.reversed_graph[node].append(i)

        no_of_strongy_component = 0
        l = len(self.dfs_stack)
        for _ in range(l):            
            element = self.dfs_stack.pop()            
            if self.visited_list[element] == 0:
                no_of_strongy_component += 1
                self.dfs(element, True)
        print("Strongly Connected Component", no_of_strongy_component)
        return no_of_strongy_component
    
def test_set1_find_strongly_connected_component():
    no_of_nodes = 8
    edges = [
        [0,1],
        [1,2],
        [2,0],
        [2,3],
        [3,4],
        [7,4],
        [4,5],
        [5,6],
        [6,4],
        [6,7]
    ]

    s = StronglyConnected(no_of_nodes ,edges)
    s.find_strongly_connected_components(0)

test_set1_find_strongly_connected_component()
    