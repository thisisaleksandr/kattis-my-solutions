from collections import Counter
n, t = map(int, input().split())
lst = [int(i) for i in input().split()]
ss = set(lst)
if t==1:
    flag = any(7777 - x in ss and x != 7777 - x for x in ss)
    print("Yes" if flag else "No")
elif t==2:
    if len(set(lst)) == n:
        print("Unique")
    else:
        print("Contains duplicate")
elif t==3:
    num = -1
    col = Counter(lst)
    for x in col:
        if col[x] > n//2:
            num = x
            break
    print(num)
elif t==4:
    if n%2==1:
        print(sorted(lst)[n//2])
    else:
        print(sorted(lst)[(n//2)-1], sorted(lst)[n//2])
elif t==5:
    newlst = sorted([j for j in lst if j in range(100, 1000)])
    print(*newlst)