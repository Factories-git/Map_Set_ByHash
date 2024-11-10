import sys
input = sys.stdin.readline

fruit = {'STRAWBERRY' : 0, 'BANANA' : 0, 'LIME' : 0, 'PLUM' : 0}
for i in range(int(input())):
    fr,ca = input().split()
    fruit[fr] += int(ca)

for f,c in fruit.items():
    if c == 5:
        print('YES')
        exit(0)
print('NO')