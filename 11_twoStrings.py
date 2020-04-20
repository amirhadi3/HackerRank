from collections import Counter

def twoStrings(s1, s2):
    S1 = Counter(s1)
    S2 = Counter(s2)
    tmp_bool = S1 & S2 != {}
    if tmp_bool:
        result = 'YES'
    else:
        result = 'NO'
    return result

s1 = "Hello"
s2 = "World"

print(twoStrings(s1, s2))
