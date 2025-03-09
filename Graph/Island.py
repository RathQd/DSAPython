from queue import Queue

NOT_VISITED = 0
VISITED = 1

class Island:
    def __init__(self):
        self.mat0 = [[0,1,1,0], [0,1,1,0], [0,0,1,0], [0,0,0,0], [1,1,0,1]]
        self.visited_list0 = [[0] * len(self.mat0[0]) for _ in range(len(self.mat0))]
        self.mat1 = [[0,1], [1,0], [0,0], [1,0]]
        self.visited_list1 = [[0]* len(self.mat1[0]) for _ in range(len(self.mat1))]
        self.mat2 = [[0,1,1,1,0,0,0,], [0,0,1,1,0,1,0]]
        self.visited_list2 = [[0] * len(self.mat2[0]) for _ in range(len(self.mat2))]

    def dfs(self, start_node, visited_list, mat):
        MaxR = len(mat)
        MaxC = len(mat[0])
        visited_list[start_node[0]][start_node[1]] = VISITED
        r = start_node[0]
        c = start_node[1]
        for dr in range(-1, 2, 1):
            for dc in range(-1, 2, 1):
                nr = r + dr
                nc = c + dc
                if (nr >=0 and nr < MaxR) and (nc >=0 and nc < MaxC) and visited_list[nr][nc] == NOT_VISITED and mat[nr][nc] == 1:
                    visited_list[nr][nc] = VISITED
                    self.dfs([nr, nc], visited_list, mat)
            

    
    def bfs(self, start_node, visited_list, mat):
        MaxR = len(mat)
        MaxC = len(mat[0])
        visited_list[start_node[0]][start_node[1]] = VISITED        
        q = Queue()
        q.put(start_node)
        while not q.empty():
            element = q.get()    
            r = element[0]
            c = element[1]                        
            for dr in range(-1, 2, 1):
                for dc in range(-1, 2, 1):
                    nr = r + dr
                    nc = c + dc                           
                    if (nr >= 0 and nr < MaxR) and (nc >=0 and nc < MaxC) and visited_list[nr][nc] == NOT_VISITED and mat[nr][nc] == 1:                        
                        visited_list[nr][nc] = VISITED
                        q.put([nr, nc])
    
    
    
    def find_number_of_island_using_bfs(self):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0        
        for row in range(len(self.mat0)):
            for col in range(len(self.mat0[0])):                
                if self.visited_list0[row][col] == NOT_VISITED and self.mat0[row][col] == 1:
                    cnt0 += 1 
                    self.bfs([row, col], self.visited_list0, self.mat0)
        print("mat0", cnt0)
        
        for row in range(len(self.mat1)):
            for col in range(len(self.mat1[0])):
                if self.visited_list1[row][col] == NOT_VISITED and self.mat1[row][col] == 1:
                    cnt1 += 1 
                    self.bfs([row, col], self.visited_list1, self.mat1)
        print("mat1", cnt1)

        for row in range(len(self.mat2)):
            for col in range(len(self.mat2[0])):                
                if self.visited_list2[row][col] == NOT_VISITED and self.mat2[row][col] == 1:
                    cnt2 += 1 
                    self.bfs([row, col], self.visited_list2, self.mat2)
        print("mat2", cnt2)


    def find_number_of_island_using_dfs(self):
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for row in range(len(self.mat0)):
            for col in range(len(self.mat0[0])):
                if self.visited_list0[row][col] == NOT_VISITED and self.mat0[row][col] == 1:
                    cnt0 += 1 
                    self.dfs([row, col], self.visited_list0, self.mat0)
        print("mat0", cnt0)

        for row in range(len(self.mat1)):
            for col in range(len(self.mat1[0])):                
                if self.visited_list1[row][col] == NOT_VISITED and self.mat1[row][col] == 1:
                    cnt1 += 1 
                    self.dfs([row, col], self.visited_list1, self.mat1)
        print("mat1", cnt1)

        for row in range(len(self.mat2)):
            for col in range(len(self.mat2[0])):                
                if self.visited_list2[row][col] == NOT_VISITED and self.mat2[row][col] == 1:
                    cnt2 += 1 
                    self.dfs([row, col], self.visited_list2, self.mat2)
        print("mat2", cnt2)
        
                    


print("BFS")
island_bfs = Island()
island_bfs.find_number_of_island_using_bfs()


print("DFS")
island_dfs = Island()
island_dfs.find_number_of_island_using_dfs()

    