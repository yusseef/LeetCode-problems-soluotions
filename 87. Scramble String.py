class Solution:
    map = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        a, b, c = [0] * 26, [0] * 26, [0] * 26
        if (s1 + s2) in self.map:
            return self.map[s1 + s2]
        for i in range(1, n):
            j = n - i
            a[ord(s1[i - 1]) - ord('a')] += 1
            b[ord(s2[i - 1]) - ord('a')] += 1
            c[ord(s2[j]) - ord('a')] += 1
            if a == b and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.map[s1 + s2] = True
                return True
            if a == c and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                self.map[s1 + s2] = True
                return True
        self.map[s1 + s2] = False
        return False