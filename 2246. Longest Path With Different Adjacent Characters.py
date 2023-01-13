import collections 
def longestPath(parent, s):
    graph = collections.defaultdict(list)

    for i, parent in enumerate(parent):
        graph[parent].append(i)
    
    ans = 1

    def dfs(node):
        nonlocal ans
        counter = second_counter = 0
        for child in graph[node]:
            length = dfs(child)
            if s[child] != s[node]:
                if length > counter:
                    second_counter = counter 
                    counter = length
                elif length > second_counter:
                    second_counter = length

        ans = max(ans, counter + second_counter + 1)
        return counter + 1
    dfs(0)
    return ans


longestPath([-1,0,0,1,1,2], "abacbe") 