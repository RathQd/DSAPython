"""
Floyed Warshall Algo
it will go from all nodes to all nodes. 
here I am using the matrix representation.

mat[r][c] = mat[r][intermidiate_node] + mat[intermidiate_node][c]
"""

class FloydWarshall:
    def __init__(self, no_of_nodes, edges):        
        self.no_of_nodes = no_of_nodes
        self.edges = edges
        self.graph_mat = [[float('inf')]*self.no_of_nodes for _ in range(no_of_nodes)]
        for i in range(self.no_of_nodes):
            self.graph_mat[i][i] = 0
        for edge in self.edges:
            node1, node2, weight = edge
            self.graph_mat[node1][node2] = weight                
        
    def find_all_pair_shortest_path(self):
        for i in range(self.no_of_nodes):            
            for r in range(self.no_of_nodes):
                for c in range(self.no_of_nodes):                    
                    new_distance = self.graph_mat[r][i] + self.graph_mat[i][c]                                                                    
                    if new_distance != float('inf') and self.graph_mat[r][c] > new_distance:                                            
                        self.graph_mat[r][c] = new_distance                                                                            
        return self.graph_mat        

def test_set1_all_pair_shortest_path():
    edges = [
        [0,2,2],
        [0,1,6],
        [0,3,4],
        [2,4,1],
        [2,1,3],
        [4,1,1],
        [3,1,1]
    ]
    no_of_nodes = 5
    f = FloydWarshall(no_of_nodes, edges)
    graph = f.find_all_pair_shortest_path()    
    for row in graph:
        print(row)

def test_set2_all_pair_shortest_path():
    edges = [
        [0,1,2],
        [1,0,1],
        [1,2,3],
        [3,0,3],
        [3,1,5],
        [3,2,4],        
    ]
    no_of_nodes = 4
    f = FloydWarshall(no_of_nodes, edges)
    graph = f.find_all_pair_shortest_path()    
    for row in graph:
        print(row)

def test_set3_all_pair_shortest_path():
    # finding the city which is having the min number of cities to reach from that node. if there are 2 cities we have to return max city.
    # distance of the city should be less than some threshold
    edges = [
        [0,1,3],
        [1,2,1],
        [1,3,4],
        [2,3,1]                
    ]
    no_of_nodes = 4
    f = FloydWarshall(no_of_nodes, edges)
    graph = f.find_all_pair_shortest_path()    
    for row in graph:
        print(row)
    
    threshold = 4    
    city = float('-inf')
    city_count = float('inf')
    for i in range(no_of_nodes):
        count = 0
        for j in range(no_of_nodes):
            if graph[i][j] <= threshold:
                count += 1
        if city_count > count:
            city_count = count
            city = i
        if city_count == count:
            city = max(city, i)
    print("City is having the list of cities distance less then threshold and which is max if there are more then 2 cities : ", city)




test_set1_all_pair_shortest_path()
test_set2_all_pair_shortest_path()
test_set3_all_pair_shortest_path()