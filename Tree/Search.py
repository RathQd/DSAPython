from Node import create_binary_search_tree
class Search:
    def __init__(self):
        self.tree = create_binary_search_tree()

    def search_element_in_tree(self, node,  key):          
        if node == None:
            return None
        if key == node.data:            
            return node.data
        elif key > node.data and node.right:
            right = self.search_element_in_tree(node.right, key)
            if right != None:
                return right
        elif node.left:
            left = self.search_element_in_tree(node.left, key)
            if left != None:
                return left
        return None
        

def search_element():
    s = Search()
    key = 100
    result = s.search_element_in_tree(s.tree, key)
    print(result)


search_element()



    