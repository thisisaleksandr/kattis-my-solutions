mtrx = [input() for _ in range(7)]

total = 0

for i in range(7):
    for j in range(7):
        if mtrx[i][j] == 'o':
            if j+2 < 7:
                if mtrx[i][j+2] == '.' and mtrx[i][j+1] == 'o':
                    total += 1
            if j-2 >= 0:
                if mtrx[i][j-2] == '.' and mtrx[i][j-1] == 'o':
                    total += 1
            if i+2 < 7:
                if mtrx[i+2][j] == '.' and mtrx[i+1][j] == 'o':
                    total += 1
            if i-2 >= 0:
                if  mtrx[i-2][j] == '.' and mtrx [i-1][j] == 'o':
                    total += 1
print(total)