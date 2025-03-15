""" Leetcode Course I and Course II graph"""

from queue import Queue
class Course:

    def __init__(self, no_of_nodes):
        self.no_of_nodes = no_of_nodes
        self.graph = [[] for _ in range(no_of_nodes+1)]        
    
    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
    
    def test_course_completion(self):
        q = Queue()
        order = []
        indegree_list = [0 for _ in range(self.no_of_nodes)]
            
        for i in range(self.no_of_nodes):
            for node in self.graph[i]:
                indegree_list[node] += 1
        
        for i in range(self.no_of_nodes):
            if indegree_list[i] == 0:
                q.put(i)

        while not q.empty():
            element = q.get()
            order.append(element)
            for node in self.graph[element]:
                indegree_list[node] -= 1
                if indegree_list[node] == 0:
                    q.put(node)    
        return order if len(order) == len(indegree_list) else False

def test_set1_course():
    # normal DAG
    c = Course(6)
    c.add_edge(0,1)
    c.add_edge(2,3)
    c.add_edge(4,5)
    c.add_edge(1,3)
    c.add_edge(2,4)
    print(c.test_course_completion())

def test_set2_course():
    # DAG with reverse edges
    c = Course(6)
    c.add_edge(1,0)
    c.add_edge(3,2)
    c.add_edge(5,4)
    c.add_edge(3,1)
    c.add_edge(4,2)    
    print(c.test_course_completion())

def test_set3_course():
    # reverse edges with cycle
    c = Course(6)
    c.add_edge(1,0)
    c.add_edge(3,2)
    c.add_edge(5,4)
    c.add_edge(3,1)
    c.add_edge(4,2)    
    c.add_edge(2,5)    
    print(c.test_course_completion())

test_set1_course()
test_set2_course()
test_set3_course()

