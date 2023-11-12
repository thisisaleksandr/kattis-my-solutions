num = int(input())
lst = []
counter = 0
for _ in range(num):
    cmd = input()
    f = 1
    for i in range(1, len(cmd)):
        if cmd[i-1] == 'C' and cmd[i] == 'D':
            f = 0
    if f==1:
        counter+=1
print(counter)