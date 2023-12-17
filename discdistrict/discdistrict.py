r = int(input())
f=1
for i in range(1, r+1):
    if f==0:
        break
    for j in range(1, r+1):
        if i**2 + j**2 > r**2:
            print(i, j)
            f = 0
            break