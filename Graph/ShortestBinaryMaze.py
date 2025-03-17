

from queue import PriorityQueue
class ShortestBinaryMaze():
    def __init__(self):
        
        self.graph = [
            [1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,0,0],
            [1,0,0,1]
        ]

        self.distance_mat = [[float('inf')]* len(self.graph[0]) for _ in range(len(self.graph))]

    def dijkstra_bfs(self, start, end):
        print(start)
        maxR = len(self.graph)
        maxC = len(self.graph[0])
        pq = PriorityQueue()
        pq.put([0, start])
        self.distance_mat[start[0]][start[1]] = 0
        while not pq.empty():
            old_distance, node = pq.get()
            if node == end:
                return old_distance
            r = node[0]
            c = node[1]
            for dr  in range(-1,2,1):
                for dc in range(-1,2,1):
                    if abs(dc) != abs(dr):
                        nr = r + dr
                        nc = c + dc
                        new_distance = old_distance + 1
                        if (nr >= 0 and nr < maxR) and (nc >= 0 and nc < maxC) and self.distance_mat[nr][nc] > (old_distance + new_distance) and self.graph[nr][nc] == 1:
                            self.distance_mat[nr][nc] = new_distance
                            pq.put([new_distance, [nr, nc]])                            
        return -1

        
def test_set1_shortest_distance():
    s = ShortestBinaryMaze()
    start = [0,1]
    end = [3, 1]
    distance = s.dijkstra_bfs(start, end)
    print(f"Shortest Distance from {start} to {end} is : ", distance)





test_set1_shortest_distance()









