from collections import Counter
from itertools import combinations

def sherlockAndAnagrams_2(s):
    count = []
    for i in range(1, len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j], 2))) for j in b]))
    return sum(count)

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    def isAnagram(s1, s2):
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        return (s1_sorted == s2_sorted)

    num_anagrams = 0
    for i in range(1, len(s)):
        for j in range(0, len(s) - i + 1):
            s1 = s[j:j + i]
            for k in range(j + 1, len(s) - i + 1):
                s2 = s[k:k + i]
                if isAnagram(s1, s2):
                    num_anagrams += 1

    return num_anagrams

s = "abba"
print(sherlockAndAnagrams_2(s))