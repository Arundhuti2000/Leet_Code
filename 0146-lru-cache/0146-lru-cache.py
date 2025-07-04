from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.c=capacity
        # self.m=dict()
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.value=self.cache[key]
        self.cache.move_to_end(key)
        return self.value
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.c:
                self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)