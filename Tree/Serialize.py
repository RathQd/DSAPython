from Node import create_binary_tree2, Node
from queue import Queue
from Traverse import Traverse

class Serialize:
    def __init__(self):
        self.tree = create_binary_tree2()
        pass

    def serialize(self, tree):
        string = []
        q = Queue()
        q.put(tree)
        while not q.empty():
            node = q.get()            
            if node ==  None:
                string.append('#')
                continue
            else:
                string.append(node.data)
            q.put(node.left)
            q.put(node.right)            
        return string

    def deserialize(self, string):
        i = 0
        q =  Queue()               
        tree = Node(string[i])
        q.put(tree)
        while not q.empty():
            l = q.qsize()
            for _ in range(l):
                i += 1
                node = q.get()                
                print(node.data)
                if string[i] != '#':
                    left = Node(string[i])
                    q.put(left)
                
                if string[i] == '#':
                    node.left = None
                else:
                    node.left = left

                i += 1
                if string[i] != '#':
                    right = Node(string[i])
                    q.put(right)

                if string[i] == '#':
                    node.right = None
                else:
                    node.right = right
        return tree

def create_serialize_string():
    s = Serialize()
    string = s.serialize(s.tree)
    return string    

def validate_serialize_string():
    string = create_serialize_string()
    s = Serialize()
    tree = s.deserialize(string)  
    trav = Traverse()  
    trav.bfs_traverse(tree)


validate_serialize_string()


