def detectCapitalUse(word):
        if word.isupper():
            return 'true'
        elif word.islower():
            return 'true'
        elif word[0].isupper() and word[1:].islower():
            return 'true'
        else:
            return 'false'


