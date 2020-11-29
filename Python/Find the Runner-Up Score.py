if __name__ == '__main__':
    n = int(input())
    x = sorted(set(map(int, input().split())))
    print(x[-2])
