class LFUCache:

    def __init__(self, capacity: int):
        # data structure 1: dictionary which maps key to count
        # data strcuture 2: dictionary which maps count to a orderedDict
        self.capacity = capacity
        self.used = 0
        self.cache_key = dict()
        self.cache_orderedCount = dict()
        self.min_cnt = 0
        

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache_key:
            val = self.cache_key[key][0]
            old_cnt = self.cache_key[key][1]
            self.cache_key[key][1] += 1
            # update the count dictionary
            del self.cache_orderedCount[old_cnt][key]
            # insert the key into the new count dictionary
            new_cnt = self.cache_key[key][1]
            self._updateCacheCountDict(key, val, new_cnt)
            # update the min count
            if self.min_cnt == old_cnt and len(self.cache_orderedCount[old_cnt]) == 0:
                self.min_cnt = new_cnt
        return val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.cache_key:
            self.cache_key[key][0] = value
            old_cnt = self.cache_key[key][1]
            self.cache_key[key][1] += 1
            new_cnt = old_cnt + 1
            del self.cache_orderedCount[old_cnt][key]
            self._updateCacheCountDict(key, value, new_cnt)
            # update the min count
            if self.min_cnt == old_cnt and len(self.cache_orderedCount[old_cnt]) == 0:
                self.min_cnt = new_cnt
        else:
            # the key is not in cache yet
            if self.used < self.capacity:
                # the cache is not full, we can directly add the new key value pair
                self.cache_key[key] = [value, 1]
                self._updateCacheCountDict(key, value, 1)
                self.used += 1
                self.min_cnt = 1
            else:
                # the cache is full
                rm_key, rm_val = self.cache_orderedCount[self.min_cnt].popitem(0)
                del self.cache_key[rm_key]
                # add new key value
                self.cache_key[key] = [value, 1]
                self._updateCacheCountDict(key, value, 1)
                self.min_cnt = 1
                
    def _updateCacheCountDict(self, key, value, new_cnt):
        if new_cnt not in self.cache_orderedCount:
            self.cache_orderedCount[new_cnt] = OrderedDict()
        self.cache_orderedCount[new_cnt][key] = value
        self.cache_orderedCount[new_cnt].move_to_end(key)