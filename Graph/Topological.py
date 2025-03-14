from Graph import create_sample_DAG1, create_sample_DAG2
from queue import Queue

NOT_VISITED = 0
VISITED = 1

class Topological:

    def __init__(self):
        self.dag = create_sample_DAG2()
        self.visited_list = [NOT_VISITED for _ in range(self.dag.get_no_nodes()+1)]
        self.stack = []

    def topology_order_dfs(self, start_node, visited_list, stack):        
        visited_list[start_node] = VISITED
        print("Start  : ",start_node)
        for node in self.dag.graph_using_list[start_node]:
            if visited_list[node[0]] == NOT_VISITED:
                visited_list[node[0]] = VISITED
                self.topology_order_dfs(node[0], visited_list, stack)
        stack.append(start_node)

    def topology_order_bfs(self, result):    
        indegree_list = [NOT_VISITED for _ in range(self.dag.get_no_nodes()+1)]
        for n in range(1, self.dag.get_no_nodes()+1):
            for node in self.dag.graph_using_list[n]:
                indegree_list[node[0]] += 1
        q = Queue()
        
        for i in range(1, len(indegree_list)):
            if indegree_list[i] == 0:
                q.put(i)

        while not q.empty():
            element = q.get()
            result.append(element)
            for node in self.dag.graph_using_list[element]:
                indegree_list[node[0]] -= 1
                if indegree_list[node[0]] == 0:
                    q.put(node[0])                                

# dag = Topological()    
# for node in range(1, dag.dag.get_no_nodes()+1):
#     if dag.visited_list[node] == NOT_VISITED:
#         dag.topology_order_dfs(node, dag.visited_list, dag.stack)
        
# for num in reversed(dag.stack):
#     print(num, end = " ")

dag1 = Topological()    
dag1.topology_order_bfs(dag1.stack)
for num in dag1.stack:
    print(num, end = " ")


