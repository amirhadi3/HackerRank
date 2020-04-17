#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    string_length = len(s)
    num_a_ins = s.count('a')
    num_a = (n // len(s)) * num_a_ins
    print(n, len(s))

    tmp_s = s[0: n % len(s)]
    num_a += tmp_s.count('a')
    return num_a

if __name__ == '__main__':

    s = 'aba'

    n = 10

    result = repeatedString(s, n)

    print(result)
