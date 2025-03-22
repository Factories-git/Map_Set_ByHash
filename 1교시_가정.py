f, ch, e, b = map(int, input().split())
fn, cn, en, bn = map(int, input().split())
cookie = 0
q = int(input())
for _ in range(q):
    c, i = map(int, input().split())
    if c == 1:
        if f >= fn * i and ch >= cn * i and e >= en * i and b >= bn * i:
            cookie += i
            f -= fn * i
            ch -= cn * i
            e -= en * i
            b -= bn * i
            print(cookie)
        else:
            print('Hello, siumii')
    elif c == 2:
        f += i
        print(f)
    elif c == 3:
        ch += i
        print(ch)
    elif c == 4:
        e += i
        print(e)
    elif c == 5:
        b += i
        print(b)