
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

