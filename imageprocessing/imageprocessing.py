h, w, n, m = map(int, input().split())
mtrx = [[int(i) for i in input().split()] for _ in range(h)]
kernel = [[int(i) for i in input().split()] for _ in range(n)]

newmtrx = [[0 for _ in range(w-m+1)] for _ in range(h-n+1)]

for k in kernel:
    k.reverse()
for x in range(n//2):
    kernel[x], kernel[-1-x] = kernel[-1-x], kernel[x]
    
for u in range(h-n+1):
    for k in range(w-m+1):
        counter = 0
        for i in range(n):
            for j in range(m):
                counter+=kernel[i][j]*mtrx[i+u][j+k]
        newmtrx[u][k] = counter
for line in newmtrx:
    print(*line)
