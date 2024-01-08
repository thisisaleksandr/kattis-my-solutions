str = input()
num = input()
a = 0
b = 1
c = 2
while c<len(num):
    x = int(num[a])*100
    y = int(num[b])*10
    z = int(num[c])
    p = x+y+z
    a += 3
    b += 3
    c += 3
    print(str[p-1], end='')