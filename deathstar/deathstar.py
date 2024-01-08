size = int(input())
mtrx = [[int(i) for i in input().split()] for _ in range(size)]
code = [0]*size

for i in range(size):
    for j in range(size):
        code[i] |= mtrx[i][j]
        code[j] |= mtrx[i][j]

print(*code)