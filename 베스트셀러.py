from collections import Counter

book = []
for i in range(int(input())):
    book.append(input())
b = Counter(book)
re = []
m = max(b.values())
for i,j in b.items():
    if j == m:
        re.append(i)
re.sort()
print(re[0])
