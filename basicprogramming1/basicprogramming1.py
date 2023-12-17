n, t = map(int, input().split())
lst = [int(i) for i in input().split()]
if t==1:
    print(7)
elif t==2:
    if lst[0]>lst[1]:
        print("Bigger")
    elif lst[0]==lst[1]:
        print("Equal")
    else:
        print("Smaller")
elif t==3:
    print(sorted([lst[0], lst[1], lst[2]])[1])
elif t==4:
    print(sum(lst))
elif t==5:
    print(sum([j for j in lst if j%2==0]))
elif t==6:
    for x in lst:
        print(chr(x%26 + 97), end='')
elif t==7:
    myset = set()
    ind = 0
    while True:
        num = lst[ind]
        myset.add(ind)
        if num > len(lst) - 1:
            print("Out")
            break
        elif num==len(lst)-1:
            print("Done")
            break
        else:
            if lst[num] in myset:
                print("Cyclic")
                break
            else:
                ind = lst[num]