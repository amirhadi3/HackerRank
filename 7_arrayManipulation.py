#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for operation in queries:
        x, y, increment = operation
        arr[x - 1] += increment
        if y <= len(arr):
            arr[y] -= increment
        print(arr)

    max_value = x = 0
    for i in arr:
        x = x + i
        if max_value < x:
            max_value = x

    return max_value


if __name__ == '__main__':
    queries = []
    n = 5
    queries = [[1, 2, 100], \
               [2, 5, 100], \
               [3, 4, 100]]

    result = arrayManipulation(n, queries)

    print(result)
