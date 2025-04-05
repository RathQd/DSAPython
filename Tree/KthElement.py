from Node import create_binary_search_tree
class KthElement:
    def __init__(self):
        self.tree = create_binary_search_tree()        
        self.count = 0
        self.no_of_nodes = 0


    def find_kth_smallest_of_tree_dfs(self, root, k):                
        if not root:
            return
        left = self.find_kth_smallest_of_tree_dfs(root.left, k)
        if left:
            return left
        self.count += 1
        if self.count == k:
            return root.data               
        right = self.find_kth_smallest_of_tree_dfs(root.right, k)
        if right:
            return right
    
    def count_number_of_nodes(self, root):
        if not root:
            return 
        self.count_number_of_nodes(root.left)
        self.no_of_nodes += 1
        self.count_number_of_nodes(root.right)


def find_kth_smallest():
    k = KthElement()
    kth_smallest = k.find_kth_smallest_of_tree_dfs(k.tree, 7)
    print(kth_smallest)

def find_kth_largest():
    k = KthElement()
    k.count_number_of_nodes(k.tree)    
    print(k.no_of_nodes)
    kth_largest = k.find_kth_smallest_of_tree_dfs(k.tree, k.no_of_nodes-4)
    print(kth_largest)

find_kth_smallest()
find_kth_largest()