from Graph import create_sample_graph
from queue import Queue

VISITED = 1
NOT_VISITED = 0

class Traverse:
    def __init__(self):
        self.graph = create_sample_graph()
        self.no_of_nodes = self.graph.get_no_nodes()
        self.visited_list = [NOT_VISITED for _ in range(self.no_of_nodes+1)]

    def bfs(self, start_node = 1):
        self.visited_list[start_node] = VISITED
        q = Queue()
        q.put([start_node, 1])

        while not q.empty():
            element = q .get()[0]
            print(element)
            for neighbor in self.graph.graph_using_list[element]:
                if self.visited_list[neighbor[0]] == NOT_VISITED:
                    self.visited_list[neighbor[0]] = VISITED
                    q.put(neighbor)

t = Traverse()
t.bfs()



