from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)

for s in strs:
    count = [0] * 26

    for c in s:
        count[ord(c) - ord("a")] += 1
    
    res[tuple(count)].append(s)

print(res.values())