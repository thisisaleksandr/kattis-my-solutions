num = int(input())
nums = sorted([int(i) for i in input().split()], reverse=True)
alice = 0
bob = 0
for i in range(len(nums)):
    if i%2==0:
        alice+=nums[i]
    else:
        bob+=nums[i]
print(alice, bob)
    