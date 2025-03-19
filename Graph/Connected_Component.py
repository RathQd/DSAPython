from Graph import create_sample_graph_for_component
from queue import Queue
import DisjointSet as Ds

NOT_VISITED = 0
VISITED = 1

class Connected_Component:
    
    def __init__(self):
        self.graph = create_sample_graph_for_component()
        self.no_of_nodes = self.graph.get_no_nodes()
        self.visited_list = [NOT_VISITED for _ in range(self.graph.get_no_nodes()+1)]
        pass

    def dfs(self, start_node = 1):
        self.visited_list[start_node] = VISITED
        for neighbor in self.graph.graph_using_list[start_node]:
            if self.visited_list[neighbor[0]] == NOT_VISITED:
                self.dfs(neighbor[0])
        pass

    def bfs(self, start_node):
        self.visited_list[start_node] = VISITED
        q = Queue()
        q.put([start_node,1])
        while not q.empty():
            element = q.get()[0]
            for neighbor in self.graph.graph_using_list[element]:
                if self.visited_list[neighbor[0]] == NOT_VISITED:
                    self.visited_list[neighbor[0]] = VISITED
                    q.put(neighbor)
    
    def find_connected_component_dfs(self):
        cnt = 0
        for node in range(1, self.no_of_nodes + 1):
            if self.visited_list[node] == NOT_VISITED:
                cnt += 1                
                self.dfs(start_node=node)
        return cnt

    def find_connected_component_bfs(self):
        cnt = 0
        for node in range(1, self.no_of_nodes+1):
            if self.visited_list[node] == NOT_VISITED:
                cnt += 1
                self.bfs(node)
        return cnt



c1 = Connected_Component()
components_dfs = c1.find_connected_component_dfs()
print("Total Connected Components : ",components_dfs)

c2 = Connected_Component()
components_bfs = c2.find_connected_component_bfs()
print("Total Connected Components : ",components_bfs)


def test_set1_number_of_connected_components_with_disjoint_set():
    # Number of Connected Components with disjoint set
    graph_mat = [
        [1,0,1],
        [0,1,0],
        [1,0,1]
    ]
    ds = Ds.DisjointSet(len(graph_mat)-1)

    for i in range(len(graph_mat)):
        for j in range(len(graph_mat[0])):                        
                if ds.find_parent(i) != ds.find_parent(j):                    
                    if graph_mat[i][j] == 1:                        
                        ds.union_of_node_with_rank(i, j)
        
    cnt = 0
    for i in range(len(ds.parent)):
        if ds.parent[i] == i:
            cnt += 1
    print("NUmber Of Connected Components", cnt)


def test_set2_number_of_connected_components_with_disjoint_set():
    graph_mat =[
        [0,1,0,0,0,0,0],
        [1,0,1,0,0,0,0],
        [0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1],
        [0,0,0,0,0,1,0]
    ]
    ds = Ds.DisjointSet(len(graph_mat)-1)
    for i in range(len(graph_mat)):
        for j in range(len(graph_mat[0])):
            if ds.find_parent(i) != ds.find_parent(j):
                if graph_mat[i][j] == 1:
                    ds.union_of_node_with_rank(i, j)
    cnt = 0
    for k in range(len(ds.parent)):
        if ds.parent[k] == k:
            cnt += 1
    print("Number of Connected Components", cnt)    

def test_set3_min_number_of_edges_to_make_components_connected_with_disjoint_set():
    edges = [
        [0,1],
        [0,3],
        [0,2],
        [1,2],
        [2,3],
        [4,5],
        [5,6],
        [7,8]
    ]
    no_of_nodes = 9    
    no_of_component = 0
    ds = Ds.DisjointSet(no_of_nodes-1)
    free_edges_count = 0
    for edge in edges:
        node1, node2 = edge
        if ds.find_parent(node1) != ds.find_parent(node2):            
            ds.union_of_node_with_rank(node1, node2)
        else:
            free_edges_count += 1


    for i in range(len(ds.parent)):
        if ds.parent[i] == i:
            no_of_component += 1
    print(ds.parent)
    print(free_edges_count, no_of_component)
    if free_edges_count >= (no_of_component-1):
        print(f"Number of edges to make graph connected with {no_of_component-1} edges")
        return no_of_component -1
    else:
        print("Can not Connect the graph")
        return -1

test_set1_number_of_connected_components_with_disjoint_set()
test_set2_number_of_connected_components_with_disjoint_set()
test_set3_min_number_of_edges_to_make_components_connected_with_disjoint_set()
                
    
    

    
    
    

    








