
""" 
**finding the shortest distance from the source in DAG using DFS**

DFS for topological seq so that only ordered list of nodes comes one after another
+
min distance list to find out the min distance to each node

"""



from Graph import create_sample_DAG1_with_weight
class Shortest:
    def __init__(self):        
        self.graph = create_sample_DAG1_with_weight()                
        self.stack = []

    def dfs(self, start_node):        
        for node in self.graph.graph_using_list[start_node]:                            
                self.dfs(node[0])
        self.stack.append(start_node)


    def find_shortest_distance_dfs(self, start_node):
        distance_list = [float('inf') for _ in range(self.graph.get_no_nodes()+1)]        
        self.dfs(start_node)
        distance_list[start_node] = 0
        for node in reversed(self.stack):
            for each in self.graph.graph_using_list[node]:
                if distance_list[each[0]] > distance_list[node] + each[1]:
                    distance_list[each[0]] = distance_list[node] + each[1]
        return distance_list               

def test_set1_DAG1():
    g = Shortest()
    print(g.find_shortest_distance_dfs(1))



test_set1_DAG1()

        

        


