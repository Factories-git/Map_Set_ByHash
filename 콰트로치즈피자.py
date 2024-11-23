t = int(input())
topping = list(map(str, input().split()))
cheese = set()
for i in topping:
    if i[-6:] == 'Cheese':
        cheese.add(i)

print('yummy' if len(cheese) == 4 else 'sad')