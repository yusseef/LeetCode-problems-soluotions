def tribonacci(n):
    t = [0, 1, 1]
    if n == 0:
        return 0
    if n == 1 or n == 2 :
        return 1

    for i in range(3, n):
        total = sum(t[-3:])
        t.append(total)

    return sum(t[-3:])


print(tribonacci(25))