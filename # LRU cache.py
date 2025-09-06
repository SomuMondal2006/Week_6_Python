# LRU cache
# https://www.geeksforgeeks.org/problems/lru-cache/1



from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def process_queries(capacity, queries):
    lru = LRUCache(capacity)
    result = []

    for query in queries:
        if query[0] == "PUT":
            lru.put(query[1], query[2])
        elif query[0] == "GET":
            result.append(lru.get(query[1]))
    return result


cap = 2
queries = [["PUT", 1, 2], ["GET", 1]]
print("Output:", process_queries(cap, queries))  

cap = 2
queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5],
           ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4],
           ["PUT", 1, 2], ["GET", 3]]
print("Output:", process_queries(cap, queries))  
