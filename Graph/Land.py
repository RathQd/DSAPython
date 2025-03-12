from queue import Queue

NOT_VISITED = 0
VISITED = 1

class Land:
    def __init__(self):
        self.mat0 = [
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 0, 1],
                    [0, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0]
                ]
        self.visited_list0 = [[0] * len(self.mat0[0]) for _ in range(len(self.mat0))]
        self.mat1 = [
                    [0, 1, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 1],
                    [0, 1, 1, 0, 1],
                    [0, 0, 0, 0, 0]
                ]
        self.visited_list1 = [[0]* len(self.mat1[0]) for _ in range(len(self.mat1))]
        self.mat2 = [
                    [0, 0, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ]
        self.visited_list2 = [[0] * len(self.mat2[0]) for _ in range(len(self.mat2))]

    
    def land_bfs(self, start_node, visited_list, mat):
        q = Queue()    
        maxR = len(mat)
        maxC = len(mat[0])
        q.put(start_node)
        while not q.empty():              
            element = q.get()   
            r = element[0]
            c = element[1]
            visited_list[r][c] = VISITED
            for dr in range(-1, 2, 1):
                for dc in range(-1, 2, 1):
                    if abs(dr) != abs(dc):
                        nr = r + dr
                        nc = c + dc
                        if (nr >=0 and nr < maxR) and (nc >= 0 and nc < maxC) and mat[nr][nc] == 1 and visited_list[nr][nc] == NOT_VISITED:
                            visited_list[nr][nc] = VISITED
                            q.put([nr,nc])



                    
def run_land_dfs(s, visited_list, mat):
    cnt1 =  0
    print("Initial Mat")
    for r in mat:
        print(r)
    maxR = len(mat)
    maxC = len(mat[0])
    
    for i in range(maxR):
        if mat[i][0] == 1:
            s.land_bfs([i,0], visited_list, mat)
        if mat[i][maxC-1]:
            s.land_bfs([i, maxC-1], visited_list, mat)
    
    for j in range(maxC):
        if mat[0][j] == 1:
            s.land_bfs([0, j], visited_list, mat)
        if mat[maxR-1][j] == 1:
            s.land_bfs([maxR-1, j], visited_list, mat)
    
    for i in range(maxR-1):
        for j in range(maxC-1):
            if mat[i][j] == 1 and visited_list[i][j] == NOT_VISITED:
                cnt1 += 1


    print("Final Mat", cnt1)
    for r in mat:
        print(r)


l = Land()

run_land_dfs(l, l.visited_list0, l.mat0)
run_land_dfs(l, l.visited_list1, l.mat1)
run_land_dfs(l, l.visited_list2, l.mat2)