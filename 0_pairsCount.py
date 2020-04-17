#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from typing import List


def sockMerchant(n, ar):
    a_dict = dict([])
    for sock in ar:
        if sock in list(a_dict.keys()):
            a_dict[sock] += 1
        else:
            a_dict.update({sock: 0})
            a_dict[sock] += 1

    num_pairs = 0

    for item in list(a_dict.keys()):
        num_pairs += (a_dict[item] // 2)

    return num_pairs


if __name__ == '__main__':
    n = 10
    ar = [1, 1,1, 2, 3, 2, 2, 1, 1, 1, 4]

    result = sockMerchant(n, ar)
    print(result)
