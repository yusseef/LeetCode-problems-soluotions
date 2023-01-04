def minimumRounds(tasks):
    minimumrounds  = 0
    count = 0
    result = set(tasks)
    for i in result:
        for j in tasks:
            if i == j:
                count += 1
        if count == 1:
            return -1
        minimumrounds += (count + 2) // 3
        count = 0
    return(minimumrounds)     
tasks = [2,2,3]
print(minimumRounds(tasks))

