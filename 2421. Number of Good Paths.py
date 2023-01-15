class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x,y):
            UF[find(x)] = find(y)
        
        tree = defaultdict(list)

        val2Nodes = defaultdict(set)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
            val2Nodes[vals[s]].add(s)
            val2Nodes[vals[e]].add(e)
        

        res = len(vals)
        

        for v in sorted(val2Nodes.keys()):

            for node in val2Nodes[v]:
                for nei in tree[node]:
                    if vals[nei] <= v:
                        union(node,nei)
            

            groupCount = defaultdict(int)
            for node in val2Nodes[v]:
                groupCount[find(node)] += 1
                
            for root in groupCount.keys():

                
                res += comb(groupCount[root],2)
     
        
        return res