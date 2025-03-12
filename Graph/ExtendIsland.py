
NOT_VISITED = 0
VISITED  = 1

class ExtendIsland:
    def __init__(self):
        self.mat0 = [
                    [0, 1, 0, 1, 1],
                    [1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1],
                    [1, 1, 0, 1, 0]
                ]
        self.visited_list0 = [[0] * len(self.mat0[0]) for _ in range(len(self.mat0))]
        self.result0 = []
        self.mat1 = [
                    [1, 0, 0, 1, 0],
                    [1, 1, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0]
                ]
        self.visited_list1 = [[0]* len(self.mat1[0]) for _ in range(len(self.mat1))]
        self.result1 = []
        self.mat2 = [
                    [1, 1, 1, 0, 1],
                    [0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 1]
                ]
        self.visited_list2 = [[0] * len(self.mat2[0]) for _ in range(len(self.mat2))]
        self.result2 = []


    def island_dfs(self, start_node, base_node, visited_list, mat, result):        
        result.append([start_node[0]- base_node[0], start_node[1]-base_node[1]])
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
                    if (nr >= 0 and nr < maxR) and (nc >= 0 and nc < maxC) and mat[nr][nc] == 1 and visited_list[nr][nc] == NOT_VISITED:
                        visited_list[nr][nc] = VISITED
                        self.island_dfs([nr, nc], base_node, visited_list, mat, result)
                        
        return result
                    



e = ExtendIsland()
def run_land_dfs(e, visited_list, mat, result):
    resultset = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and visited_list[i][j] == NOT_VISITED:
                e.island_dfs([i, j], [i, j], visited_list, mat, result)
                l = tuple(tuple(r) for r in result)
                result = []            
                resultset.add(l)
    print("Identical Islands", len(resultset))
    for i in resultset:
        print(i)

run_land_dfs(e, e.visited_list0, e.mat0, e.result0)
run_land_dfs(e, e.visited_list1, e.mat1, e.result1)
run_land_dfs(e, e.visited_list2, e.mat2, e.result2)
