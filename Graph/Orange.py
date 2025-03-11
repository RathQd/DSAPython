from queue import Queue

NOT_VISITED = 0
VISITED = 1

class Orange:
    def __init__(self):
        self.mat0 = [[2,1,1], [1,1,0], [0,0,1]]
        self.visited_list0 = [[0] * len(self.mat0[0]) for _ in range(len(self.mat0))]
        self.mat1 = [[0,1,2], [0,1,2], [2,1,1]]
        self.visited_list1 = [[0]* len(self.mat1[0]) for _ in range(len(self.mat1))]
        self.mat2 = [[0,1,2], [0,1,1], [2,1,1]]
        self.visited_list2 = [[0] * len(self.mat2[0]) for _ in range(len(self.mat2))]
        self.roten = 2
        self.fresh = 1
    
    def bfs(self, visited_list, mat):
        time = 0
        fresh_count = 0
        maxR = len(mat)
        maxC = len(mat[0])
        q = Queue()
        for i in range(maxR):
            for j in range(maxC):
                if mat[i][j] == self.roten:
                    visited_list[i][j] = self.roten
                    q.put([[i,j],0])
                if mat[i][j] == self.fresh:
                    fresh_count += 1
                    
        
        while not q.empty():
            element = q.get()
            r =  element[0][0]
            c = element[0][1]
            if time < element[1]:
                time = element[1]
            for dr in range(-1, 2, 1):
                for dc in range(-1, 2, 1):
                    nr = r + dr
                    nc = c + dc
                    if (nr>=0 and nr<maxR) and (nc >0 and nc < maxC) and visited_list[nr][nc] != self.roten and mat[nr][nc] == self.fresh:
                        visited_list[nr][nc] = self.roten
                        fresh_count -= 1
                        q.put([[nr,nc], element[1]+1])
        
        # for i in range(maxR):
        #     for j in range(maxC):
        #         if mat[i][j] == self.fresh and visited_list[i][j] != self.roten:
        #             return -1

        # optimized code for the above loop
        
        if fresh_count > 0:
            return -1
        
        return time

                

            


            
        

orangeBoard = Orange()
print("Time Taken for mat0", orangeBoard.bfs(orangeBoard.visited_list0, orangeBoard.mat0))
print("Time Taken for mat1", orangeBoard.bfs(orangeBoard.visited_list1, orangeBoard.mat1))
print("Time Taken for mat1", orangeBoard.bfs(orangeBoard.visited_list2, orangeBoard.mat2))
    
