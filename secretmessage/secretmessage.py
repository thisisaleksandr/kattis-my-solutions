from math import sqrt

num = int(input())
for _ in range(num):
    word = input()
    leng = len(word)
    kv = int(sqrt(leng-0.00001))+1
    word += "*"*((kv**2)-leng)
    i = 0
    mtrx = []
    while i < kv**2:
        mtrx.append(word[i: i+kv])
        i += kv
    newword = ''
    for x in range(kv):
        for y in range(kv):
            if mtrx[kv-1-y][x] != '*':
                newword += mtrx[kv-1-y][x]
    print(newword)