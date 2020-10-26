import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = str(bin(n))
    max = 0
    counter = 0
    for x in binary:
        if x == '1':
            counter += 1
        else:
            if counter > max:
                max = counter
            counter = 0

    if counter > max:
        max = counter

    print(max)
