import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    s = n-1
    for i in range(1, n+1):
        for c in range(s):
            print(' ', end='')
        for j in range(i):
            print('#', end='')
        s -= 1
        print("")
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
