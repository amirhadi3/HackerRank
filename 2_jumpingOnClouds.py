#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    index = 0
    jump_counter = 0
    done = False

    while not done:
        next_index = index+2
        if next_index > len(c)-1:
            next_index = index + 1

        if c[next_index] == 0:
            jump_counter += 1
            index = next_index

        elif c[next_index-1] == 0:
            index = next_index-1
            jump_counter += 1

        if index == len(c)-1:
            done = True

    return jump_counter

if __name__ == '__main__':

    c = [0, 0, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    print(result)
