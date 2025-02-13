n, c = map(int, input().split())
frequency = {}
sequence = list(map(int, input().split()))
for j in range(n):
    i = sequence[j]
    if i in frequency:
        frequency[i][0] += 1
    else:
        frequency[i] = [1, j]
sequence.sort(key=lambda x:(-frequency[x][0], frequency[x][1]))
print(*sequence)