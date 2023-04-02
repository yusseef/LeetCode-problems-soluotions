n = 6
counter = 0
for i in range(1,n + 1):
    if n % i == 0:
        print(i)
        counter += 1
print(counter)