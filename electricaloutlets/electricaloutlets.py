num = int(input())
for _ in range(num):
    lst = [int(i) for i in input().split()]
    counter=0
    for strip in lst[1:]:
        counter+=(strip-1)
    print(counter+1)