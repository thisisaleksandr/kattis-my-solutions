num = int(input())
for _ in range(num):
    nums = input().split()
    x = int(nums[1])
    sum_pos = 0
    sum_odd = 0
    sum_even = 0
    for i in range(1, x+1):
        if i>0:
            sum_pos+=i
    for j in range(1, x*2+1):
        if j%2==1:
            sum_odd+=j
        else:
            sum_even+=j
    print(nums[0], sum_pos, sum_odd, sum_even)