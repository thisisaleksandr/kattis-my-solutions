lst = sorted(map(int, input().split()))
dif1 = lst[1]-lst[0]
dif2 = lst[2]-lst[1]
if dif2>dif1:
    print(lst[1]+dif1)
elif dif2<dif1:
    print(lst[0]+dif2)
elif dif2==dif1:
    print(lst[2]+dif1)