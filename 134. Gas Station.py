def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total, gasplus, s = len(gas), 0, 0, 0

        for i in range(n):
            total += gas[i] - cost[i]
            gasplus += gas[i] - cost[i]
            if gasplus < 0:
                gasplus = 0
                s = i + 1
        
        return -1 if (total < 0) else s