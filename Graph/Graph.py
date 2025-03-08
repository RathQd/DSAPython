class Graph:
    def __init__(self, no_of_nodes):
        self.no_of_nodes = no_of_nodes
        self.graph_matrix = [[0]*(no_of_nodes+1) for _ in range(no_of_nodes+1)]
        self.graph_using_list = [[] for _ in range(no_of_nodes+1)]
    
    def add_edge_in_matrix(self, node1, node2, weight=1):
        self.graph_matrix[node1][node2] = weight
        self.graph_matrix[node2][node1] = weight
    
    def add_edge_in_list(self,node1, node2, weight_to_r=1, weight_to_l=1, directed=False):
        self.graph_using_list[node1].append([node2,weight_to_r])
        if not directed:
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
    graph.add_edge_in_list(2,4)
    graph.add_edge_in_list(3,5)
    graph.add_edge_in_list(4,5)
    graph.add_edge_in_list(4,6)
    graph.add_edge_in_list(5,6)

    graph.display_graph_as_using_list()
    return graph

