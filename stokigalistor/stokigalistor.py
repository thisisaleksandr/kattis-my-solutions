num = int(input())
lst = [int(i) for i in input().split()]
lst2 = sorted(lst)
counter = 0
for i in range(len(lst)):
    if lst[i] != lst2[i]:
        counter+=1
print(counter)