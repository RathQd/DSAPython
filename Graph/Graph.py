class Graph:
    def __init__(self, no_of_nodes):
        self.no_of_nodes = no_of_nodes
        self.graph_matrix = [[0]*(no_of_nodes+1) for _ in range(no_of_nodes+1)]
        self.graph_using_list = [[] for _ in range(no_of_nodes+1)]
    
    def add_edge_in_matrix(self, node1, node2, weight=1):
        self.graph_matrix[node1][node2] = weight
        self.graph_matrix[node2][node1] = weight
    
    def add_edge_in_list(self,node1, node2, weight=1, weight_to_r=1, weight_to_l=1, directed=False, bidirect = False):
        if not directed:
            self.graph_using_list[node1].append([node2,weight])
            self.graph_using_list[node2].append([node1,weight]) 
        else:             
            self.graph_using_list[node1].append([node2,weight_to_r])
            if bidirect:
                self.graph_using_list[node2].append([node1,weight_to_l]) 
            

    def display_graph_as_matrix(self):
        for row in self.graph_matrix:
            print(row)
    
    def display_graph_as_using_list(self):
        for node_row in self.graph_using_list:
            print(node_row)
    
    def get_no_nodes(self):
        return self.no_of_nodes




def create_sample_graph():
    no_of_nodes = 6
    graph = Graph(no_of_nodes)

    # graph.add_edge_in_matrix(1,2)
    # graph.add_edge_in_matrix(2,3)
    # graph.add_edge_in_matrix(2,4)
    # graph.add_edge_in_matrix(1,5)
    # graph.add_edge_in_matrix(4,5)

    # graph.display_graph_as_matrix()

    graph.add_edge_in_list(1,2)
    graph.add_edge_in_list(1,3)
    graph.add_edge_in_list(2,3)
    graph.add_edge_in_list(4,2)
    graph.add_edge_in_list(3,5)
    graph.add_edge_in_list(4,5)
    graph.add_edge_in_list(4,6)
    graph.add_edge_in_list(5,6)

    graph.display_graph_as_using_list()
    return graph


def create_sample_graph_for_component():
    no_of_nodes = 10

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(1,2)
    graph.add_edge_in_list(2,3)
    graph.add_edge_in_list(4,5)
    graph.add_edge_in_list(5,6)
    graph.add_edge_in_list(6,7)
    graph.add_edge_in_list(4,7)
    graph.add_edge_in_list(8,9)
    graph.add_edge_in_list(5,7)
    graph.add_edge_in_list(10,9)
    graph.add_edge_in_list(10,8)
    return graph

def create_sample_graph_for_cycle():
    no_of_nodes = 8

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(1,2)
    graph.add_edge_in_list(1,3)
    graph.add_edge_in_list(2,5)
    graph.add_edge_in_list(5,6)
    # graph.add_edge_in_list(3,1)
    graph.add_edge_in_list(3,4)
    # graph.add_edge_in_list(3,6)
    graph.add_edge_in_list(5,7)
    # graph.add_edge_in_list(6,3)
    graph.add_edge_in_list(6,7)

    return graph

def create_sample_graph_for_bipartite():
    no_of_nodes = 12

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(1,2)
    graph.add_edge_in_list(2,3)
    graph.add_edge_in_list(3,4)
    graph.add_edge_in_list(3,6)
    graph.add_edge_in_list(4,5)
    graph.add_edge_in_list(4,6)
    graph.add_edge_in_list(6,7)
    graph.add_edge_in_list(5,8)
    graph.add_edge_in_list(7,8)
    graph.add_edge_in_list(8,9)
    graph.add_edge_in_list(9,10)
    graph.add_edge_in_list(10,11)
    graph.add_edge_in_list(10,12)

    return graph


def create_sample_directed_graph1():
    no_of_nodes = 12

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(1,2, directed= True)
    graph.add_edge_in_list(2,3, directed= True)
    graph.add_edge_in_list(3,4, directed= True)
    graph.add_edge_in_list(6,3, directed= True)
    graph.add_edge_in_list(4,5, directed= True)
    graph.add_edge_in_list(4,6, directed= True)
    graph.add_edge_in_list(7,6, directed= True)
    graph.add_edge_in_list(5,8, directed= True)
    graph.add_edge_in_list(8,7, directed= True)
    graph.add_edge_in_list(8,9, directed= True)
    graph.add_edge_in_list(9,10, directed= True)
    graph.add_edge_in_list(10,11, directed= True)
    graph.add_edge_in_list(10,12, directed= True)

    return graph

def create_sample_directed_graph2():
    no_of_nodes = 5

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(1,2, directed= True)
    graph.add_edge_in_list(2,3, directed= True)
    graph.add_edge_in_list(3,4, directed= True)
    graph.add_edge_in_list(4,5, directed= True)
    # add below one for cycle
    graph.add_edge_in_list(5,2, directed= True)
    
    return graph

def create_sample_DAG1():
    no_of_nodes = 10

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(1,2, directed= True)
    graph.add_edge_in_list(1,3, directed= True)
    graph.add_edge_in_list(2,6, directed= True)
    graph.add_edge_in_list(3,4, directed= True)
    graph.add_edge_in_list(4,5, directed= True)
    graph.add_edge_in_list(5,7, directed= True)
    graph.add_edge_in_list(6,7, directed= True)
    graph.add_edge_in_list(7,8, directed= True)
    graph.add_edge_in_list(7,9, directed= True)
    graph.add_edge_in_list(8,9, directed= True)
    graph.add_edge_in_list(9,10, directed= True)
    return graph


def create_sample_DAG2():
    no_of_nodes = 6

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(6,2, directed= True)
    graph.add_edge_in_list(2,3, directed= True)
    graph.add_edge_in_list(2,4, directed= True)
    graph.add_edge_in_list(3,4, directed= True)
    graph.add_edge_in_list(3,5, directed= True)
    graph.add_edge_in_list(3,1, directed= True)
    graph.add_edge_in_list(5,1, directed= True)
    
    return graph

def create_sample_DAG1_with_weight():
    no_of_nodes = 8

    graph = Graph(no_of_nodes)
    
    graph.add_edge_in_list(1,2, weight_to_r=1, directed= True)
    graph.add_edge_in_list(1,6, weight_to_r=2, directed= True)
    graph.add_edge_in_list(2,3, weight_to_r=3, directed= True)
    graph.add_edge_in_list(6,3, weight_to_r=1, directed= True)
    graph.add_edge_in_list(3,7, weight_to_r=1, directed= True)
    graph.add_edge_in_list(3,4, weight_to_r=2, directed= True)
    graph.add_edge_in_list(3,8, weight_to_r=3, directed= True)
    graph.add_edge_in_list(4,5, weight_to_r=1, directed= True)
    graph.add_edge_in_list(8,5, weight_to_r=1, directed= True)
    graph.add_edge_in_list(7,4, weight_to_r=1, directed= True)
    return graph

def create_sample_undirected_graph_with_weight():
    no_of_nodes = 8
    graph = Graph(no_of_nodes)

    graph.add_edge_in_list(1,2)
    graph.add_edge_in_list(2,4)
    graph.add_edge_in_list(2,3)
    graph.add_edge_in_list(2,6)
    graph.add_edge_in_list(3,7)
    graph.add_edge_in_list(4,8)
    graph.add_edge_in_list(3,5)
    graph.add_edge_in_list(3,6)
    graph.add_edge_in_list(5,7)
    graph.add_edge_in_list(7,8)
    graph.add_edge_in_list(6,7)
    return graph