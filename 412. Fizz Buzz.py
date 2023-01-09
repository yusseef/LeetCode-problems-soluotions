
def fizzBuzz( n):
    arr = [x for x in range(1, n+1)]
    lst = []
    for i in arr:
        if i % 3 == 0 and i % 5 ==0:
            lst.append("FizzBuzz")
        elif i % 3 ==0:
            lst.append("Fizz")

        elif i % 5 ==0:
            lst.append("Buzz")
        
        
        else:
            lst.append(str(i))


    return lst
print(fizzBuzz(3))
