
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(graph,curr,res,labels):
            currCounter = Counter([labels[curr]])
            if curr not in graph:
                return currCounter, res
            if not graph[curr]:
                return {},res
            children = graph[curr]
            graph[curr] = set([])
            for c in children:
                tempCounter, res = dfs(graph,c,res,labels)
                currCounter += tempCounter
            res[curr] = currCounter[labels[curr]]
            return currCounter, res
        
        graph = {}
        for edge in edges:
            fr,to = edge
            if fr not in graph:
                graph[fr] = set([])
            graph[fr].add(to)
            if to not in graph:
                graph[to] = set([])
            graph[to].add(fr)

        res = [1]*len(labels)
        dfs(graph,0,res,labels)
        return res