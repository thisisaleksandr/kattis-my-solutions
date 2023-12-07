num = int(input())
nums = list(map(int, input().split()))
sortnums = sorted(nums, reverse=True)
counter = 0
for i in range(num):
    if sortnums[i]+(i+1)>counter:
        counter = sortnums[i] + i+1
print(counter+1)