from collections import Counter, defaultdict


# Complete the checkMagazine function below.
def checkMagazine_sol1(magazine, note):
    tmp_bool = (Counter(note) - Counter(magazine)) == {}
    if tmp_bool:
        print('Yes')
    else:
        print('No')


def checkMagazine_sol2(magazine, note):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word] += 1
    for word in note:
        if dicty[word] == 0: return False
        dicty[word] -= 1
    return True


magazine = 'This is a a a a a good snowy weather'.split()
note = 'snowy weather is good'.split()
checkMagazine_sol1(magazine, note)
