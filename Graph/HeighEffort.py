"""
GFG Path with Minimum Efforts Question
PQ is using [diff, [row, col]]
"""

from queue import PriorityQueue
class HeightEffort:
    def __init__(self, graph):
        self.graph = graph
        self.effort_mat = [[float('inf')] * len(self.graph[0]) for _ in range(len(self.graph))]

    def dijkstra_for_minimum_effort(self, start, end):
        maxR = len(self.graph)
        maxC = len(self.graph[0])
        pq = PriorityQueue()
        pq.put([0, start])
        self.effort_mat[start[0]][start[1]] = 0
        while not pq.empty():
            old_diff, node = pq.get()            
            if node == end:
                return old_diff                
            r = node[0]
            c = node[1]
            for dr in range(-1,2,1):
                for dc in range(-1,2,1):
                    if abs(dr) != abs(dc):
                        nr = r + dr
                        nc = c + dc                        
                        if(nr >= 0 and nr < maxR) and (nc >= 0 and nc < maxC):                            
                            new_diff = max(abs(self.graph[r][c] - self.graph[nr][nc]), old_diff)
                            if  self.effort_mat[nr][nc] > new_diff:                                
                                self.effort_mat[nr][nc] = new_diff
                                pq.put([new_diff,[nr, nc]])
        return -1

def test_set1_for_minimum_effort():
    Heights = [
        [1,2,2],
        [3,8,2],
        [5,3,5]
    ]
    h = HeightEffort(Heights)
    start = [0,0]
    end = [2,2]
    result = h.dijkstra_for_minimum_effort(start, end)
    print(result)

def test_set2_for_minimum_effort():
    Heights =[
        [1,2,1,1,1],
        [1,2,1,2,1],
        [1,2,1,2,1],
        [1,1,1,2,1]
    ]
    h = HeightEffort(Heights)
    start = [0,0]
    end = [3,4]
    result = h.dijkstra_for_minimum_effort(start, end)
    print(result)

test_set1_for_minimum_effort()    
test_set2_for_minimum_effort()    