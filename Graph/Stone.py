from DisjointSet import DisjointSet

class Stone:
    def __init__(self, no_of_stone, stones):
        self.no_of_stone = no_of_stone
        self.stones = stones                
        max_point_stone = max(self.stones)
        self.maxR = max_point_stone[0]
        self.maxC = max_point_stone[1]
        no_of_nodes = self.maxR + self.maxC +1
        self.ds = DisjointSet(no_of_nodes)        
        
    
    def find_max_no_stone_to_remove(self):
        for stone in self.stones:
            node1 = stone[0]
            node2 = self.maxR + stone[1] + 1            
            if self.ds.find_parent(node1) != self.ds.find_parent(node2):
                self.ds.union_of_node_with_size(node1, node2)        

        no_of_component = 0
        parents = set()
        for i in range(len(self.ds.parent)):
            if self.ds.parent[i] == i:
                no_of_component += 1
                parents.add(i)
        
        no_of_valid_component = 0
        valid_parents = set()
        for stone in self.stones:
            node1 = stone[0]
            node2 = self.maxR + stone[1] + 1
            valid_parents.add(node1)
            valid_parents.add(node2)
        
        for p in parents:
            if p in valid_parents:
                no_of_valid_component += 1        
        
        return self.no_of_stone - no_of_valid_component
        
def test_set1_remove_stone():
    no_of_stone = 6
    stones = [[0,0], [0,2], [1,3], [3,0], [3,2], [4,3]]    

    s = Stone(no_of_stone, stones)
    stone_removed = s.find_max_no_stone_to_remove()
    print("Max Stone Can be Removed : ", stone_removed)

    pass


test_set1_remove_stone()