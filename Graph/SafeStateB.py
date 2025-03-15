"""
safeSateNode = whose all path are ending at the terminal node
terminal node = whose outdegree is 0

"""

from queue import Queue
class SafeStateBFS:

    def __init__(self, no_of_nodes):
        self.no_of_nodes = no_of_nodes
        self.graph = [[] for _ in range(self.no_of_nodes+1)]        
        pass

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        pass

    def find_all_safe_state_nodes(self):
        q = Queue()
        order = []
        indegree_list = [0 for _ in range(self.no_of_nodes+1)]

        for i in range(self.no_of_nodes+1):
            for node in self.graph[i]:
                indegree_list[node] += 1

        for i in range(self.no_of_nodes+1):
            if indegree_list[i] == 0:
                q.put(i)
                
        while not q.empty():
            element = q.get()
            order.append(element)
            for node in self.graph[element]:
                indegree_list[node] -= 1
                if indegree_list[node] == 0:
                    q.put(node)
        return list(reversed(order)) if len(order) == len(indegree_list)-1 else False
                

def test_set1_graph():
    g = SafeStateBFS(19)
    g.add_edge(2,1)
    g.add_edge(3,2)
    g.add_edge(4,3)
    g.add_edge(13,4)
    g.add_edge(14,4)
    g.add_edge(15,13)
    g.add_edge(15,14)
    g.add_edge(16,15)
    g.add_edge(17,15)
    g.add_edge(16,17)
    g.add_edge(18,16)
    g.add_edge(6,1)
    g.add_edge(8,6)
    g.add_edge(6,11)
    g.add_edge(8,10)
    g.add_edge(9,8)
    g.add_edge(10,9)
    g.add_edge(10,12)
    g.add_edge(19,10)
    g.add_edge(11,10)
    print(g.find_all_safe_state_nodes())

test_set1_graph()    
