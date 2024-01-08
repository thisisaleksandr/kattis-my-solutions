num = int(input())
m = [int(i) for i in input().split()]
c1 = [int(k) for k in input().split()]
c2 = [int(j) for j in input().split()]

for z in range(num):
    x = (m[z], c1[z], c2[z])
    y = sorted(x)
    print(y[1], end=" ")