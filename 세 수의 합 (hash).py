n = int(input())
arr = sorted((int(input()) for _ in range(n)))
bout = []
for i in arr:
    for j in arr:
        bout.append(i+j)
bout = set(bout)
flag = True
for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if arr[i] - arr[j] in bout:
            print(arr[i])
            flag = False
            break
    if not flag:
        break