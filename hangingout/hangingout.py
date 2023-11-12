nums = input().split()
a = int(nums[0])
b = int(nums[1])
c = a;
counter = 0
for i in range(b):
    group = input().split()
    num = int(group[1])
    if group[0]=="enter":
        if num <= c:
            c -= num
        else:
            counter+=1
    elif group[0]=="leave":
        c += num
print(counter)