import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    while n >0:
        print(str(arr[n-1]) + " ",end="")
        n -= 1