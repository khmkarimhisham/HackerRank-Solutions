
import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    # print(math.factorial(n))
    fact = 1
    for i in range(2,n+1):
        fact *= i
    print(fact)
    
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)