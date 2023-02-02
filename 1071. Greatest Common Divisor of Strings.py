def gcdOfStrings(str1, str2):
    i = (str1*2).find(str1, 1)
    x = (str2*2).find(str2, 1)

    if str1[:i] == str2[:x]:
        return str1[:i]
    else:
        return ""

