
from DisjointSet import DisjointSet

class LargestIsland:    
    def __init__(self, graph):
        self.graph = graph
        self.maxR = len(self.graph)
        self.maxC = len(self.graph[0])        
        self.ds = DisjointSet((self.maxR * self.maxC))                
    
    def find_largest_island(self):
        for r in range(self.maxR):
            for c in range(self.maxC):                
                if self.graph[r][c] == 1:                    
                    parent_node = ((r*self.maxC) + c)                
                    # print(f"parent with r {r} and c {c}",parent_node)
                    for dr in range(-1,2,1):
                        for dc in range(-1,2,1):
                            if abs(dr) != abs(dc):                                                            
                                nr = r + dr
                                nc = c + dc
                                child_node = ((nr*self.maxC) + nc)                            
                                if (nr >= 0 and nr < self.maxR and nc >=0 and nc < self.maxC) and self.graph[nr][nc] == 1:
                                    # print("child node", child_node)
                                    if self.ds.find_parent(child_node) != self.ds.find_parent(parent_node):
                                        self.ds.union_of_node_with_size(parent_node, child_node)

        # print("Size", self.ds.size)
        # print("Parent", self.ds.parent)
        # print("Connected", self.ds.is_belong_to_same_component(1,3))
        # print("Parent of Node", self.ds.find_parent(3))

        result = []
        for r in range(self.maxR):
            for c in range(self.maxC):
                if self.graph[r][c] == 0:                    
                    temp = set()
                    temp_size = []
                    for dr in range(-1,2,1):
                        for dc in range(-1,2,1):
                            if abs(dr) != abs(dc):
                                nr = r + dr
                                nc = c + dc
                                if (nr >=0 and nr < self.maxR and nc >=0 and nc < self.maxC) and self.graph[nr][nc] == 1:
                                    child_node = (nr * self.maxC + nc)
                                    child_extrm_parent = self.ds.find_parent(child_node)                                                                   
                                    temp.add(child_extrm_parent)                                    
                    for eligible_child_node in temp:
                        temp_size.append(self.ds.size[eligible_child_node])
                    result.append(sum(temp_size)+1)
        
        return result












def test_set1_find_largest_island():
    
    graph = [
        [1,1,0,1,1],
        [1,1,0,1,1],
        [1,1,0,1,1],
        [0,0,1,0,0],
        [0,0,1,1,1],
        [0,0,1,1,1]
    ]

    largestIsland = LargestIsland(graph)
    number_of_ones_in_largest_island = largestIsland.find_largest_island()
    print(number_of_ones_in_largest_island)


def test_set2_find_largest_island():       

    graph = [
        [1,1,0,1,1],
        [1,1,0,1,1],
        [1,1,0,0,1]       
    ]

    largestIsland = LargestIsland(graph)
    number_of_ones_in_largest_island = largestIsland.find_largest_island()
    print(number_of_ones_in_largest_island)


def test_set3_find_largest_island():       

    graph = [
        [1,0],
        [0,0]      
    ]

    largestIsland = LargestIsland(graph)
    number_of_ones_in_largest_island = largestIsland.find_largest_island()
    print(number_of_ones_in_largest_island)


test_set1_find_largest_island()
test_set2_find_largest_island()
test_set3_find_largest_island()



    
    


