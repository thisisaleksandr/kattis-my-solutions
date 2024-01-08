nums = [int(i) for i in input().split()]
mtrx = []
r = nums[0]
c = nums[1]
zr = nums[2]
zc = nums[3]
for j in range(r):
    mtrx.append(list(input()))

new_mtrx = []
for k in range(r):
    line = ''
    for p in range(c):
        line += mtrx[k][p]*zc
    for z in range(zr):
        new_mtrx.append(line)
for row in new_mtrx:
    print(row)