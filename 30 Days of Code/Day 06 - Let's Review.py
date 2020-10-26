t = int(input())
for x in range(t):
    s=str(input())
    a=''
    b=''
    for c in range(len(s)):
        if c%2==0:
            a+=s[c]
        elif c%2==1:
            b+=s[c]
    print(a + ' ' + b)
        