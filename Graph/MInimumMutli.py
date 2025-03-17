

from queue import Queue
class MinimumMulti:
    def __init__(self, num, start, end, mod):
        self.num = num
        self.start = start
        self.end = end        
        self.mod = mod
        self.num_list = [float('inf') for _ in range(mod)]
    
    def find_minimum_step(self):
        q = Queue()
        q.put([0, self.start])        
        self.num_list[self.start] = 0
        while not q.empty():
            prev_step, prev_num = q.get()        
            if prev_num == self.end:
                return prev_step
            for prime in self.num:
                new_num = (prev_num * prime) % self.mod
                if self.num_list[new_num] > (prev_step + 1):
                    self.num_list[new_num] = prev_step + 1
                    q.put([(prev_step+1), new_num])
        return -1

def test_set1_min_multiplication_step():
    num = [2,5,7]
    start = 3
    end = 600
    mod = 100000
    m = MinimumMulti(num, start, end, mod)
    print(m.find_minimum_step())


test_set1_min_multiplication_step()