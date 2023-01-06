def maxIceCream(costs, coins):
    counter = 0
    costs.sort()
    for i in costs:
        if i <= coins:
            coins -= i
            counter += 1