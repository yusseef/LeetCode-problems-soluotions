def isPalindrome(x):
        y = str(x)[::-1]
        if x == y:
            return 'true'
        else:
            return 'false'

result = isPalindrome(-121)
