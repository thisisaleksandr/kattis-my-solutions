items, sec = map(int, input().split())
lst = [int(input()) for _ in range(items)]
lst = sorted(lst, reverse=True)
flag = True
while len(lst) != 0:
    if lst[0] <= (len(lst) - 1)*sec:
        flag = False
        break
    del lst[0]
if flag==True:
    print("YES")
else:
    print("NO")