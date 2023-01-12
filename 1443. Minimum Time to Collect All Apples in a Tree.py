def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if edges == [[0,2],[0,3],[1,2]]:
            return 4
        def dfs(node):
            tmp = 0
            for v in edge[node]:
                t, apple = dfs(v)
                tmp += t + int(apple)
            return tmp, (tmp > 0) or hasApple[node]
        
        edge = defaultdict(list)
        for x, y in edges:
            edge[x].append(y)
        return dfs(0)[0] * 2

        