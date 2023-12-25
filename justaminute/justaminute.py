tc = int(input())

minut = 0
sec = 0
for _ in range(tc):
    m, s = map(int, input().split())
    minut += m*60
    sec += s


total = sec/minut
if total > 1:
    print(sec/minut)
else:
    print("measurement error")
