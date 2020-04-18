#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    d = d % len(a)
    tmp_a = a[0:d]
    a = a[d:]+tmp_a

    #for counter in range(0, d):
        #tmp_a = a[1:len(a)]
        #tmp_a.append(a[0])
        #a = tmp_a

    return a


if __name__ == '__main__':
    d = 6

    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)

    print(result)
