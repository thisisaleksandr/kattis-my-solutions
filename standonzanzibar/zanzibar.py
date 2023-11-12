a = int(input())

for _ in range(a):
    lst = [int(i) for i in input().split()]
    odin = 1
    counter = 0
    for k in range(1, len(lst)):
        if lst[k]>odin*2:
            counter += (lst[k]-(odin*2))
            odin = lst[k]
        else:
            odin = lst[k]
    print(counter)