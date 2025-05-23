s = input()
ls = len(s)
s_ = set()
for i in range(1, ls+1):
    for j in range(ls):
        s_.add(s[j:j+i])
print(len(s_))