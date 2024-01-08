num = int(input())

for _ in range(num):
    lst = [int(i) for i in input().split()]
    lst = lst[1:]
    for j in range(1, len(lst)-1):
        if lst[j-1] != lst[j]-1:
            print(j+1)
            break