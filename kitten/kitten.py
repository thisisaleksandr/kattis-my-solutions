num = int(input())

lst = []
path = set()
path.add(num)

nums = list(map(int, input().split()))

while nums[0]!=-1:
    lst.append(nums)
    nums = list(map(int, input().split()))
    
for i in range(len(lst)):
    if num in lst[i] and num!=lst[i][0]:
        inx = i

root = lst[inx][0]
path.add(root)

while True:
    for j in range(len(lst)):
        if root in lst[j] and root!=lst[j][0]:
            root = lst[j][0]
            path.add(root)
    if root in lst[0]:
      path.add(lst[0][0])
      break
    
print(*path)
