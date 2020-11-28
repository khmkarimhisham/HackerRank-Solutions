import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus = minus = zero = 0
    for x in arr:
        if x > 0:
            plus += 1
        elif x < 0:
            minus += 1
        else:
            zero += 1
    print("{:0.6f}".format(plus/len(arr)))
    print("{:0.6f}".format(minus/len(arr)))
    print("{:0.6f}".format(zero/len(arr)))
    
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
