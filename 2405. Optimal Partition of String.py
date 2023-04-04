class Solution:
    def partitionString(self, s: str) -> int:
        cur_set = set()
        counter = 1
        for i in s:
            if i in cur_set:
                counter += 1
                cur_set.clear()
            cur_set.add(i)
        return counter
        


