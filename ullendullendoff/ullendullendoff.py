num = int(input())
names = input().split()
k = 13
while k>=num:
    k-=num
print(names[k-1])