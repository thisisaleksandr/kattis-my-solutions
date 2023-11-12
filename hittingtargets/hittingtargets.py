num = int(input())
figures = []
for _ in range(num):
    lst = input().split()
    figures.append(lst)
    
shots = int(input())    
for _ in range(shots):
    shoot = [int(i) for i in input().split()]
    x = shoot[0]
    y = shoot[1]
    counter = 0
    for n in figures:
        if n[0]=='rectangle':
            if x>=int(n[1]) and x<=int(n[3]) and y>=int(n[2]) and y<=int(n[4]):
                counter+=1
        if n[0]=='circle':
            if ((x-int(n[1]))**2 + (y-int(n[2]))**2) <= int(n[3])**2:
                counter+=1
    print(counter)