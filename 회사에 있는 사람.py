import sys

input = sys.stdin.readline
s = []
log = {}
for i in range(int(input())):
    name, act = input().split()
    log[name] = act
for i,j in log.items():
    if log[i] == 'enter':
        s.append(i)
s.sort(reverse=True)
for i in s:
    print(i)