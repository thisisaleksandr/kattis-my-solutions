a, b = map(int, input().split())
mtrx = [input() for _ in range(a)]
message = ''
for i in range(a):
    for j in range(b):
        if mtrx[i][j].isalpha():
            message+=mtrx[i][j]
print(message)