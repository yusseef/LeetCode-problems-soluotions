
def maximumWealth(accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        arr = []
        for account in accounts:
            arr.append(sum(account))
        res = max(arr)
        return res

print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))