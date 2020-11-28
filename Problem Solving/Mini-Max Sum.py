import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum, min, max = 0, sys.maxsize, -sys.maxsize
    for i in arr:
        sum += i
        if(i > max):
            max = i
        if(i < min):
            min = i
    print(str(sum-max) + ' ' + str(sum-min))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
