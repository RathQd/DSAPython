from DisjointSet import DisjointSet

class Wordladder:    
    SEA = 0
    LAND = 1
    def __init__(self, row, col, ds_object, queries):
        self.no_of_islands = 0
        self.queries = queries
        self.graph = [[0]*col for _ in range(row)]
        self.maxC = col
        self.maxR = row
        self.ds_object = ds_object
        self.seq = []
        
    def find_no_of_island_seq(self):        
        for query in self.queries:
            r = query[0]
            c = query[1]
            if self.graph[r][c] == Wordladder.SEA:
                self.graph[r][c] = Wordladder.LAND
                self.no_of_islands += 1
                for dr in range(-1, 2, 1):
                    for dc in range(-1,2,1):
                        if abs(dr) != abs(dc):
                            nr = r + dr
                            nc = c + dc
                            if (nr >= 0 and nr < self.maxR and nc >= 0 and nc < self.maxC) and self.graph[nr][nc] == Wordladder.LAND:                                                                                  
                                node1 = r*self.maxC + c
                                node2 = nr*self.maxC + nc
                                if self.ds_object.find_parent(node1) != self.ds_object.find_parent(node2):
                                    self.ds_object.union_of_node_with_rank(node1, node2)        
                                    self.no_of_islands -= 1              
            self.seq.append(self.no_of_islands)
        return self.seq
                    

def test_set1_no_of_island_seq_word_ladder():
    n = 4
    m = 5
    queries = [(0,0), (0,0), (1,1), (1,0), (0,1), (0,3), (1,3), (0,4), (3,2), (2,2), (1,2), (0,2)]    
    ds = DisjointSet(n*m)
    w = Wordladder(row=n, col=m, ds_object=ds, queries=queries)
    seq = w.find_no_of_island_seq()
    print("Number of Island Seq per Query: ",seq)


test_set1_no_of_island_seq_word_ladder()