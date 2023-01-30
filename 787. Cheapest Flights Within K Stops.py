
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph, dis = defaultdict(list), [-1 for _ in range(n)]
        for f, to, price in flights:
            graph[f].append([to, price])

        dis[src], q, step = 0, deque([src]), 0

        while q and step <= k:
            sz = len(q)
            new_dis = list(dis)
            for _ in range(sz):
                cur = q.popleft()
                for neighbor in graph[cur]:
                    if new_dis[neighbor[0]] == -1 or new_dis[neighbor[0]] > dis[cur]+neighbor[1]:
                        new_dis[neighbor[0]] = dis[cur] + neighbor[1]
                        q.append(neighbor[0])
            step += 1
            dis = new_dis

        return dis[dst]