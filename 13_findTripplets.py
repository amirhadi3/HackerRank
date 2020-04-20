import math
import re
from collections import Counter, defaultdict

def countTriplets(arr, r):
    if r == 1:
        count_dict = Counter(arr)
        num = 0
        for item in count_dict:
            n = count_dict[item]
            if n > 2:
                num += int(math.factorial(n)/(math.factorial(3)*math.factorial(n-3)))
    else:
        count_dict = defaultdict()
        count_dict['size_1'] = defaultdict(int)
        count_dict['size_2'] = defaultdict(int)
        count_dict['size_3'] = defaultdict(int)

        for number in arr:
            count_dict['size_1'][number] += 1
            if number % r == 0:
                count_dict['size_2'][number // r] += count_dict['size_1'][number // r]
            if number % r**2 == 0:
                count_dict['size_3'][number // (r**2)] += count_dict['size_2'][number // (r**2)]

        num = sum(count_dict['size_3'].values())

    return num

arr = [1,5,5,5,25,5,125,6,8,2,10,50]
r = 5
print(countTriplets(arr,r))