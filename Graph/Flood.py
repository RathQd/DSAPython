from queue import Queue

class Flood:
    def __init__(self):
        # self.mat = [[1,1,1], [2,2,0], [2,2,2]]
        self.mat = [
            [0,1,1,0,1,0],
            [0,0,0,0,1,0],
            [0,0,1,1,1,0],
            [0,0,0,1,1,1],
            [0,0,0,1,0,1],
            [0,2,0,1,0,1],
            [1,1,1,1,1,1]

        ]
        self.visited_list = self.mat.copy()
        self.pcolor = 1
        self.ncolor = 5

    def bfs(self, start_node):
        maxR = len(self.mat)
        maxC = len(self.mat[0])
        q = Queue()
        q.put(start_node)
        while not q.empty():
            element = q.get()
            r = element[0]
            c = element[1]        
            if self.visited_list[r][c] != self.ncolor and self.mat[r][c] == self.pcolor:                
                self.visited_list[r][c] = self.ncolor
                for dr in range(-1, 2, 1):
                    for dc in range(-1, 2, 1):
                        if abs(dr) != abs(dc):                            
                            nr = r + dr
                            nc = c + dc
                            if (nr >= 0 and nr < maxR) and (nc >=0 and nc < maxC) and self.mat[nr][nc] == self.pcolor:                                
                                q.put([nr, nc])


    def dfs(self, start_node):        
        maxR = len(self.mat)
        maxC = len(self.mat[0])        
        r = start_node[0]
        c = start_node[1]
        if self.mat[r][c] == self.pcolor and self.visited_list[r][c] != self.ncolor:            
            self.visited_list[r][c] = self.ncolor
            for dr in range(-1, 2, 1):
                for dc in range(-1, 2, 1):
                    if abs(dr) != abs(dc):
                        nr = r + dr
                        nc = c + dc
                        if (nr >= 0 and nr < maxR) and (nc >= 0 and nc < maxC) and self.mat[nr][nc] == self.pcolor:                                                        
                            self.dfs([nr, nc])

    def flood_fill_algo_with_dfs(self, start_node):
        self.dfs(start_node)
    
    def flood_fill_algo_with_bfs(self, start_node):
        self.bfs(start_node)


f = Flood()
f.flood_fill_algo_with_dfs([0,4])
for r in f.visited_list:
    print(r)


print(" ")


f1 = Flood()
f1.flood_fill_algo_with_bfs([0,4])
for r in f1.visited_list:
    print(r)

if f1.visited_list == f.visited_list:
    print("True")    



        