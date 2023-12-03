tc = int(input())

for _ in range(tc):
    lst = int("".join([i for i in input().split()]))
    lst2 = int("".join([j for j in input().split()]))
    print(*tuple(str(lst+lst2)))