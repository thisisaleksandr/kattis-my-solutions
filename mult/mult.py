num = int(input())
nums = [int(input()) for _ in range(num)]
while len(nums)>0:
    start = nums[0]
    i = 0
    for nextnum in nums[1:]:
        i+=1
        if nextnum%start==0:
            print(nextnum)
            break
    nums = nums[i+1:]