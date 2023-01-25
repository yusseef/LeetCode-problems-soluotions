class Solution:
    def dfs(self, node, dist, edges, dis):
        """
        Helper function to perform depth first search
        """
        # iterate until we reach the end of the edge or a node that has already been visited
        while node != -1 and dis[node] == -1:
            dis[node] = dist
            dist += 1 # update distance of current node
            node = edges[node] # move to next node

    def closestMeetingNode(self, edges, node1, node2):
        """
        Function that returns the closest meeting point between two nodes
        """
        res, min_dist, n = -1, float('inf'), len(edges)
        # create distance vectors for both nodes
        dist1, dist2 = [-1]*n, [-1]*n
        # perform DFS starting from node1 and node2
        self.dfs(node1, 0, edges, dist1)
        self.dfs(node2, 0, edges, dist2)

        # iterate through all nodes
        for i in range(n):
            # check if current node is the closest meeting point
            if min(dist1[i], dist2[i]) >= 0 and max(dist1[i], dist2[i]) < min_dist:
                min_dist = max(dist1[i], dist2[i])
                res = i
        return res
