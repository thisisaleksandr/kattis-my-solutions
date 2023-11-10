line = input().split()
a = int(line[0])
b = int(line[1])
if a>=b:
    for i in range(b+1, a+2):
        print(i)
else:
    for i in range(a+1, b+2):
        print(i)