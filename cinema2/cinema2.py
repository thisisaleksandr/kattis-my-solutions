seats, groups = map(int, input().split())
nums = [int(i) for i in input().split()]
counter = 0
left = 0
for i in range(len(nums)):
    if counter+nums[i] <= seats:
        counter+=nums[i]
    else:
        left = len(nums[i:])
        break
print(left)