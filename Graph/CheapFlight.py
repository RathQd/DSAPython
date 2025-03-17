
from queue import PriorityQueue
class CheapFlight:
    def __init__(self, flights, no_of_cities, start, end, k):        
        self.flights = flights
        self.graph = [[] for _ in range(no_of_cities)] 
        for flight in self.flights:
            self.graph[flight[0]].append([flight[1], flight[2]])            
        self.distance_list = [float('inf') for _ in range(no_of_cities)]
        self.no_of_cities = no_of_cities
        self.start = start
        self.end = end
        self.k = k


    def dijkstra_for_cheap_path(self):     
        for nod in self.graph:
            print(nod)
        pq = PriorityQueue()
        pq.put([0, 0, self.start])        
        self.distance_list[self.start] = 0
        while not pq.empty():
            k, amount, node = pq.get()                                   
            for child in self.graph[node]:                                
                child_node, child_amount = child                                                    
                new_amount = amount + child_amount                
                if k <= self.k and new_amount < self.distance_list[child_node]:
                    self.distance_list[child_node] = new_amount                                         
                    pq.put([k+1, new_amount, child_node])
        if self.distance_list[self.end] == float('inf'):
            return -1
        else:
            return self.distance_list[self.end]

def test_set1_cheap_flight():
    flights = [
            [0,1,100],
            [1,2,100],
            [2,0,100],
            [1,3,600],
            [2,3,200]
        ]
    no_of_cities = 4
    no_of_routes = len(flights)
    start = 0
    end = 3
    k = 1 # at most we allow connecting flight with k city
    f = CheapFlight(flights, no_of_cities, start, end, k)
    print(f.dijkstra_for_cheap_path())


def test_set2_cheap_flight():
    flights = [
            [0,1,5],
            [0,3,2],
            [3,1,2],
            [1,4,1],
            [4,2,1],
            [1,2,5]
        ]
    no_of_cities = 5
    no_of_routes = len(flights)
    start = 0
    end = 2
    k = 2 # at most we allow connecting flight with k city
    f = CheapFlight(flights, no_of_cities, start, end, k)
    print(f.dijkstra_for_cheap_path())

test_set1_cheap_flight()
test_set2_cheap_flight()