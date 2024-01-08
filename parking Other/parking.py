lst = list(map(int, input().split()))

nums = []
pairs = []
for _ in range(3):
    x, y = map(int, input().split())
    nums += [x, y]
    pairs.append((x, y))

total = 0

for i in range(min(nums), max(nums)+1):
    count = -1
    for time in pairs:
        if i in range(time[0], time[1]):
            count+=1
    if count>=0:
        total += lst[count]*(count+1)

print(total)
    