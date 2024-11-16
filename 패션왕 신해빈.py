for i in range(int(input())):
    gears = {}
    for _ in range(int(input())):
        name, gear = input().split()
        if gears.get(gear) is None:
            gears[gear] = [name]
        else:
            gears[gear].append(name)
    cnt = 1
    for k in gears:
        cnt *= (len(gears[k])+1)
    print(cnt-1)