x = input()
y = input()

if x=='0' or y == '0':
    print(0)
else:
    scount_x = x.count('S')
    scount_y = y.count('S')
    res = scount_x * scount_y
    for i in range(res):
        print("S(", end = "")
    print(0, ")"*res, sep='')