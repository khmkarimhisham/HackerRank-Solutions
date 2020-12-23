N = int(input())
l = list()
for i in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
    elif len(cmd) == 3:
        cmd[1] = int(cmd[1])
        cmd[2] = int(cmd[2])
    if cmd[0] == 'insert':
        l.insert(cmd[1], cmd[2])
    elif cmd[0] == 'print':
        print(l)
    elif cmd[0] == 'remove':
        l.remove(cmd[1])
    elif cmd[0] == 'append':
        l.append(cmd[1])
    elif cmd[0] == 'sort':
        l.sort()
    elif cmd[0] == 'pop':
        l.pop()
    elif cmd[0] == 'reverse':
        l.reverse()