
NOT_VISITED = 0
VISITED = 1

class Surround:
    def __init__(self):
        self.mat0 = [
                    ['X', 'X', 'X', 'X', 'X'],
                    ['O', 'O', 'X', 'O', 'X'],
                    ['X', 'X', 'X', 'O', 'X'],
                    ['X', 'X', 'O', 'X', 'O'],
                    ['X', 'X', 'O', 'X', 'O'],
                    ['X', 'X', 'X', 'X', 'X']
                ]
        self.visited_list0 = [[0] * len(self.mat0[0]) for _ in range(len(self.mat0))]
        self.mat1 = [
                    ['X', 'O', 'X', 'X', 'X'],
                    ['X', 'O', 'O', 'O', 'X'],
                    ['X', 'X', 'X', 'O', 'X'],
                    ['X', 'O', 'X', 'X', 'O'],
                    ['X', 'O', 'O', 'X', 'O'],
                    ['X', 'X', 'X', 'X', 'X']
                ]
        self.visited_list1 = [[0]* len(self.mat1[0]) for _ in range(len(self.mat1))]
        self.mat2 = [
                    ['X', 'X', 'O', 'X', 'X'],
                    ['O', 'X', 'O', 'O', 'X'],
                    ['X', 'X', 'X', 'X', 'X'],
                    ['X', 'O', 'O', 'X', 'O'],
                    ['X', 'X', 'O', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X']
                ]
        self.visited_list2 = [[0] * len(self.mat2[0]) for _ in range(len(self.mat2))]
        
        
    def surround_dfs(self, start_node, visited_list, mat):
        maxR = len(mat)
        maxC = len(mat[0])
        r = start_node[0]
        c = start_node[1]     
        visited_list[r][c] = VISITED
        for dr in range(-1, 2, 1):
            for dc in range(-1, 2, 1):
                if abs(dr) != abs(dc):
                    nr = r + dr
                    nc = c + dc 
                    if (nr >=0 and nr< maxR) and (nc>=0 and nc < maxC) and mat[nr][nc] != 'X' and visited_list[nr][nc] == NOT_VISITED:
                        self.surround_dfs([nr, nc], visited_list, mat)


def run_surround_dfs(s, mat, visited_list):
    print("Initial Mat")
    for row in mat:
        print(row)       
    maxR = len(mat)
    maxC = len(mat[0])
    for i in range(maxC):
        if mat[0][i] == 'O':
            s.surround_dfs([0,i], visited_list, mat)
        if s.mat0[maxR-1][i] == 'O':
            s.surround_dfs([maxR-1, i], visited_list, mat)

    for j in range(maxR):
        if mat[j][0] == 'O':
            s.surround_dfs([j, 0], visited_list, mat)
        if s.mat0[j][maxC-1] == 'O':
            s.surround_dfs([j, maxC-1], visited_list, mat)    

    for i in range(1, maxR-1):
        for j in range(1, maxC-1):        
            if mat[i][j] == 'O' and visited_list[i][j] == NOT_VISITED:
                mat[i][j] = 'X'
    print("Final Mat")
    for row in mat:
        print(row)
        

s = Surround()
run_surround_dfs(s, s.mat0, s.visited_list0)
run_surround_dfs(s, s.mat1, s.visited_list1)
run_surround_dfs(s, s.mat2, s.visited_list2)








                    
                    

