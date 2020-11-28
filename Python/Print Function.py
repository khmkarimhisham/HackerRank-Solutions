if __name__ == '__main__':
    n = int(input())
    x=1
    a=''
    while x!=n:
        a+=str(x)
        x += 1
    a+=str(n)
    print (a)