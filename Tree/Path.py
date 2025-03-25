from Node import create_binary_tree2

class Path:
    def __init__(self):
        self.tree = create_binary_tree2()
    
    def dfs_path(self, node, destination, path):
        if node == None:
            return 
        path.append(node.data)
        if node.data == destination:
            return path
        l = self.dfs_path(node.left, destination, path)
        r = self.dfs_path(node.right, destination, path)
        if l:            
            return path
        if r:
            return path
        path.pop()

    def find_path_from_root_to_node(self, root, destination):
        path = []
        path = self.dfs_path(root, destination, path)        
        return path if path else False

def find_path():
    p = Path()
    return p.find_path_from_root_to_node(p.tree, 9)        

print(find_path())
