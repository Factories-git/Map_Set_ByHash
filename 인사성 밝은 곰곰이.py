import sys

input = sys.stdin.readline

visit = {}
c = 0
for i in range(int(input())):
    s = input().strip()
    if s != 'ENTER':
        if s not in visit:
            visit[s] = 1
            c += 1
    else:
        visit.clear()
print(c)