from decimal import Decimal, ROUND_HALF_UP

grade_point = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0,
               'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}
c = 0
e = 0
for i in range(20):
    _, pt, gr = input().split()
    pt = float(pt)
    if gr == 'P':
        continue
    c += pt * grade_point[gr]
    e += pt

# 결과를 소수점 4자리까지 정확하게 반올림
result = Decimal(c / e).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
print(result)
