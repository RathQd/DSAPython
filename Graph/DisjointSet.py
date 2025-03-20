class DisjointSet:
    def __init__(self, no_of_nodes):
        self.no_of_nodes = no_of_nodes
        self.rank = [0] * (self.no_of_nodes+1)
        self.size = [1] * (self.no_of_nodes+1)
        self.parent = [i for i in range(self.no_of_nodes+1)]


    def find_parent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_of_node_with_size(self, node1, node2):
        
        extrm_parent_of_node1 = self.find_parent(node1)
        extrm_parent_of_node2 = self.find_parent(node2)
        
        if self.size[extrm_parent_of_node1] == self.size[extrm_parent_of_node2]:
            self.parent[extrm_parent_of_node1] = extrm_parent_of_node2
        elif self.size[extrm_parent_of_node1] < self.size(extrm_parent_of_node2):
            self.parent[extrm_parent_of_node2] = extrm_parent_of_node1
        elif self.size(extrm_parent_of_node2) < self.size(extrm_parent_of_node1):
            self.parent[extrm_parent_of_node1] = extrm_parent_of_node2


    def union_of_node_with_rank(self, node1, node2):
        
        extrm_parent_node1 = self.find_parent(node1)
        extrm_parent_node2 = self.find_parent(node2)        

        if self.rank[extrm_parent_node1] == self.rank[extrm_parent_node2]:
            self.parent[extrm_parent_node1] = extrm_parent_node2
            self.rank[extrm_parent_node1] += 1
        elif self.rank[extrm_parent_node1] > self.rank[extrm_parent_node2]:
            self.parent[extrm_parent_node1] = extrm_parent_node2
        elif self.rank[extrm_parent_node2] > self.rank[extrm_parent_node1]:
            self.rank[extrm_parent_node2] = extrm_parent_node1
    
    def is_belong_to_same_component(self, node1, node2):
        if self.find_parent(node1) == self.find_parent(node2):
            return True
        else: 
            return False


def test_set1_disjoint_set_with_rank():
    print("Disjoint Set DS with Rank")
    no_of_nodes = 7
    disjointset = DisjointSet(no_of_nodes)    
    disjointset.union_of_node_with_rank(1,2)
    disjointset.union_of_node_with_rank(2,3)
    result = disjointset.is_belong_to_same_component(1,3)
    print("Is 1 and 3 belong to same component", result)
    disjointset.union_of_node_with_rank(4,5)
    disjointset.union_of_node_with_rank(6,7)
    result = disjointset.is_belong_to_same_component(1,4)
    print("Is 1 and 4 belong to same component", result)
    disjointset.union_of_node_with_rank(5,6)
    result = disjointset.is_belong_to_same_component(3,7)
    print("Is 3 and 7 belong to same component", result)
    disjointset.union_of_node_with_rank(3,7)
    result = disjointset.is_belong_to_same_component(3,7)
    print("Is 3 and 7 belong to same component", result)

def test_set2_disjoint_set_with_size():
    print("Disjoint Set DS with Size")
    no_of_nodes = 7
    disjointset = DisjointSet(no_of_nodes)    
    disjointset.union_of_node_with_size(1,2)
    disjointset.union_of_node_with_size(2,3)
    result = disjointset.is_belong_to_same_component(1,3)
    print("Is 1 and 3 belong to same component", result)
    disjointset.union_of_node_with_size(4,5)
    disjointset.union_of_node_with_size(6,7)
    result = disjointset.is_belong_to_same_component(1,4)
    print("Is 1 and 4 belong to same component", result)
    disjointset.union_of_node_with_size(5,6)
    result = disjointset.is_belong_to_same_component(3,7)
    print("Is 3 and 7 belong to same component", result)
    disjointset.union_of_node_with_size(3,7)
    result = disjointset.is_belong_to_same_component(3,7)
    print("Is 3 and 7 belong to same component", result)

test_set1_disjoint_set_with_rank()
test_set2_disjoint_set_with_size()