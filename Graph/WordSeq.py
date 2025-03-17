

from queue import Queue
class WordSeq:
    def __init__(self):        
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        pass

    def find_shortest_trasformation_seq_length(self, start, end, words_list):
        q = Queue()
        q.put([start, 1])
        words_set = set(words_list)

        while not q.empty():
            element = q.get()
            word = element[0]
            seql = element[1]
            if word == end:
                return seql            
            for i in range(len(word)):
                temp_word_list = list(word)
                for alphabet in self.alphabets:
                    temp_word_list[i] = alphabet
                    new_word = "".join(temp_word_list)
                    if new_word in words_set:
                        q.put([new_word, seql+1])
                        words_set.discard(new_word)                
    
    
    
    def find_all_shortest_trasformation_seq(self, start, end, words_list):
        q = Queue()
        q.put([start])
        words_set = set(words_list)
        level = 0
        result = []
        onLevelElements = []
        while not q.empty():
            element = q.get()            
            if len(element) > level:
                level += 1
                for e in onLevelElements:
                    words_set.discard(e)                                              
            word = element[-1]
            if word == end:
                if len(result) == 0:
                    result.append(element)
                else:
                    if len(result[0]) == len(element):
                        result.append(element)
                             
            for i in range(len(word)):
                temp_word_list = list(word)
                for alphabet in self.alphabets:
                    temp_word_list[i] = alphabet
                    new_word = "".join(temp_word_list)               
                    onLevelElements.append(new_word)     
                    if new_word in words_set:                        
                        element.append(new_word)
                        new_list = element.copy()                            
                        q.put(new_list)                                    
                        element.remove(new_word)                        
                            
        return result             



def test_set1_WordSeq():
    w = WordSeq()
    startWord = "der"
    targetWord = "dfs"
    wordList = {"des", "der", "dfr", "dgt", "dfs"}
    seq_length = w.find_shortest_trasformation_seq_length(startWord, targetWord, wordList)
    return seq_length


def test_set2_WordSeq():
    w = WordSeq()
    startWord = "hit"
    targetWord = "cog"
    wordList = {"hot", "dot", "dog", "lot", "log", "cog"}
    seq_length = w.find_shortest_trasformation_seq_length(startWord, targetWord, wordList)
    return seq_length


def test_set3_WordSeq():
    w = WordSeq()
    startWord = "hit"
    targetWord = "cog"
    wordList = {"hot", "dot", "dog", "lot", "log", "cog"}
    seq = w.find_all_shortest_trasformation_seq(startWord, targetWord, wordList)
    return seq

print(test_set1_WordSeq())
print(test_set2_WordSeq())
print(test_set3_WordSeq())



