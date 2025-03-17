"""
creating the graph based on the occurence of the alphabet in the words, then using the topology sort of the graph getting the sequence.
"""


from queue import Queue
class AlienDict:
    def __init__(self, no_of_words, no_of_alphabets,words_list):
        self.graph = [[] for _ in range(no_of_alphabets+1)]
        self.no_of_words = no_of_words
        self.no_of_alphabets = no_of_alphabets
        self.words_list = words_list
        self.conversion_dict = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
            'w': 23, 'x': 24, 'y': 25, 'z': 26
        }
        self.reversed_conversion_dict = {value:key for key, value in self.conversion_dict.items()}
    
    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
    
    def add_changed_alphabets_in_graph(self, word1, word2):
        for i, j in zip(word1, word2):
            if i != j:
                self.add_edge(self.conversion_dict[i], self.conversion_dict[j])
                return True
        return False
    
    def find_order_of_alphabets(self):
        q = Queue()
        order = []
        for i in range(self.no_of_words-1):            
            if self.add_changed_alphabets_in_graph(self.words_list[i], self.words_list[i+1]) == False:
                if len(self.words_list[i]) > len(self.words_list[i+1]):                
                    return "empty"


        indegree_list = [0 for _ in range(self.no_of_alphabets+1)]

        for i in range(len(indegree_list)):
            for node in self.graph[i]:
                indegree_list[node] += 1
        for i in range(1, len(indegree_list)):
            if indegree_list[i] == 0:
                q.put(i)
        
        while not q.empty():
            element = q.get()
            order.append(element)
            for node in self.graph[element]:
                indegree_list[node] -= 1
                if indegree_list[node] == 0:
                    q.put(node)
        return(
              [self.reversed_conversion_dict[order[i]] for i in range(len(order))] 
              if len(order) == len(indegree_list)-1 else False)
                
def test_set1_aliend():
    N = 5
    K = 4
    Words = ["baa", "abcd", "abca", "cab", "cad"]
    
    a = AlienDict(N, K, Words)
    print(a.find_order_of_alphabets())


def test_set2_aliend():
    N = 2
    K = 4
    Words = ["abcd", "abc"]
    
    a = AlienDict(N, K, Words)
    print(a.find_order_of_alphabets())

def test_set3_aliend():
    N = 4
    K = 6
    Words = ["ab", "cd", "ef", "ad"]
    
    a = AlienDict(N, K, Words)
    print(a.find_order_of_alphabets())


def test_set4_aliend():
    N = 3
    K = 6
    Words = ["ab", "aa", "a"]
    
    a = AlienDict(N, K, Words)
    print(a.find_order_of_alphabets())

def test_set5_aliend():
    N = 5
    K = 5
    Words = ["ab", "abc", "bcd", "cd", "d"]
    
    a = AlienDict(N, K, Words)
    print(a.find_order_of_alphabets())


test_set1_aliend()
test_set2_aliend()
test_set3_aliend()
test_set4_aliend()
test_set5_aliend()
    
            

        













    
    
    
    

    
