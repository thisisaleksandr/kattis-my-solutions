def sorting(nums):
    if nums!=sorted(nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                print(*nums)
        sorting(nums)
        
line = list(map(int, input().split()))
sorting(line)