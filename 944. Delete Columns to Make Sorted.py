def minDeletionSize(strs):
    counter = 0
    for words in zip(*strs):
        if list(words) != sorted(words):
            counter += 1
    return counter


print(minDeletionSize(["abc", "bce", "cae"]))