n, k = map(int, input().split())
nums = [int(i) for i in input().split()]
q = n/k
for j in range(k-1, len(nums), k):
    print(nums[j], end=' ')