from Node import create_binary_search_tree
class Floor:
    def __init__(self):
        self.tree = create_binary_search_tree()
        pass

    def find_floor(self, node, key):
        floor = -1
        while node:
            if key == node.data:
                floor = node.data
                return floor
            elif key > node.data:
                floor = node.data
                node = node.right
            else:
                node = node.left
        return floor


def find_floor_of_key():
    f = Floor()
    floor = f.find_floor(f.tree, 100)
    print(floor)

find_floor_of_key()