class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(string):
            return string == string[::-1]
        
        def backtrack(start, partition, partitions):
            if start == len(s):
                partitions.append(partition)
                return
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    backtrack(i+1, partition + [s[start:i+1]], partitions)
        
        partitions = []
        backtrack(0, [], partitions)
        return partitions