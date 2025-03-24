from Node import create_binary_tree
from queue import Queue

class Traverse:
    def __init__(self):
        self.tree = create_binary_tree()

    def pre_order_traverse(self, root):
        if root == None:
            return
        print(root.data)
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)

    def in_order_traverse(self, root):
        if root == None:
            return
        self.in_order_traverse(root.left)
        print(root.data)
        self.in_order_traverse(root.right)
    
    def post_order_traverse(self, root):
        if root == None:
            return
        self.post_order_traverse(root.left)
        self.post_order_traverse(root.right)
        print(root.data)
    
    def bfs_traverse(self, root):
        q = Queue()
        q.put(root)        
        while not q.empty():
            node = q.get()            
            print(node.data, end=" ")
            if node.right != None and node.left != None:
                q.put(node.left)
                q.put(node.right)         
    
    def level_order_store(self, root):
        q = Queue()
        q.put(root)
        node_level_wise = []
        while not q.empty():
            loop = q.qsize()
            level_elements = []
            for _ in range(loop):                
                node = q.get()
                if node.left != None and node.right != None:
                    q.put(node.left)
                    q.put(node.right)
                level_elements.append(node.data)
            node_level_wise.append(level_elements)
        print(node_level_wise)
                        
    def dfs_traverse(self, root):        
        if root == None:
            return
        print(root.data, end=" ")
        self.dfs_traverse(root.left)
        self.dfs_traverse(root.right)
    
    def pre_order_iterative(self, root):
        # root, left, right
        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()     
            print(node.data, end =" ")       
            if node.left != None and node.right != None:
                stack.append(node.right)
                stack.append(node.left) 
    
    def in_order_iterative(self, root):
        # left, root, right
        stack = []
        stack.append(root)
        node = root
        while len(stack) > 0:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 1:
                    break
                node = stack.pop()
                print(node.data, end = " ")                
                node = node.right    

    def post_order_iterative_using_2_stacks(self, root):        
        # left, right, root
        stack1 = []
        stack2 = []
        stack1.append(root)
        while len(stack1) > 0:
            node = stack1.pop()            
            if node != None:
                stack2.append(node.data)
                stack1.append(node.left)
                stack1.append(node.right)
        
        while len(stack2) > 0:
            node = stack2.pop()
            print(node, end=" ")
    
    def post_order_iterative_using_1_stack(self, root):
        post_order = []
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                temp = stack[-1].right                            
                if temp == None:
                    temp = stack.pop()
                    post_order.append(temp.data)
                    while len(stack) != 0 and temp == stack[-1].right:
                        temp = stack.pop()
                        post_order.append(temp.data)                        
                else:
                    cur = temp
        
        for i in post_order:
            print(i, end = " ")
    
    def all_three_orders_traverse(self, root):
        stack = []
        pre_order = []
        in_order = []
        post_order = []
        stack.append([root, 1])
        while len(stack) > 0:
            node, num = stack[-1]
            if num == 1:
                pre_order.append(node.data)
                stack[-1][1] += 1
                if node.left != None:
                    stack.append([node.left,1])
            if num == 2:
                in_order.append(node.data)
                stack[-1][1] += 1
                if node.right != None:
                    stack.append([node.right,1])
            if num == 3:
                post_order.append(node.data)
                stack.pop()
        print("Pre_Order", pre_order)
        print("In_Order", in_order)
        print("Post_Order", post_order)










def traverse_tree():
    traverse =  Traverse()
    print("BFS Order")
    traverse.bfs_traverse(traverse.tree)
    print()
    print("DFS Order")
    traverse.dfs_traverse(traverse.tree)
    print()
    print("Level Order Wise")
    traverse.level_order_store(traverse.tree)
    print()
    print("Pre Order Iterative")
    traverse.pre_order_iterative(traverse.tree)
    print()
    print("In Order Iterative")
    traverse.in_order_iterative(traverse.tree)
    print()
    print("Post Order Iterative using 2 stacks")
    traverse.post_order_iterative_using_2_stacks(traverse.tree)
    print()
    print("Post Order Iterative using 1 stack")
    traverse.post_order_iterative_using_1_stack(traverse.tree)
    print()
    print("All Three Traversal")
    traverse.all_three_orders_traverse(traverse.tree)


traverse_tree()