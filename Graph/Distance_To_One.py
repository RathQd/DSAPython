from queue import Queue

NOT_VISITED = 0
VISITED = 1

class Distance_To_One:
    def __init__(self):
        self.mat0 = [[0,0,0], [0,1,0], [1,0,1]]
        self.visited_list0 = [[0] * len(self.mat0[0]) for _ in range(len(self.mat0))]
        self.distance1 = [[0] * len(self.mat0[0]) for _ in range(len(self.mat0))]

        self.mat1 = [[0,1,2], [0,1,2], [2,1,1]]
        self.visited_list1 = [[0]* len(self.mat1[0]) for _ in range(len(self.mat1))]
        self.mat2 = [[0,1,2], [0,1,1], [2,1,1]]
        self.visited_list2 = [[0] * len(self.mat2[0]) for _ in range(len(self.mat2))]
        self.roten = 2
        self.fresh = 1
    
    def bfs_for_distance(self, mat, visited_list, distance):
        q = Queue()
        maxR = len(mat)
        maxC = len(mat[0])
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    distance[r][c] = 0
                    visited_list[r][c] = VISITED
                    q.put([[r,c], 0])

        while not q.empty():            
            element = q.get()
            r = element[0][0]
            c = element[0][1]            
            for dr in range(-1, 2, 1):
                for dc in range(-1, 2, 1):
                    if abs(dr) != abs(dc):
                        nr = r + dr
                        nc = c + dc
                        if (nr >= 0 and nr < maxR) and (nc >=0 and nc < maxC) and visited_list[nr][nc] == NOT_VISITED:                                                    
                            visited_list[nr][nc] = VISITED
                            distance[nr][nc] = element[1] + 1                         
                            q.put([[nr, nc], element[1]+1])
        print(distance)



d = Distance_To_One()                        
d.bfs_for_distance(d.mat0, d.visited_list0, d.distance1)