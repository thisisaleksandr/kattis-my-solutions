while True:
    w, l = map(int, input().split())
    if w==0 and l==0:
       break
    robloc = [0, 0]
    current = [0, 0]
    tc = int(input())
    for _ in range(tc):
        x, y = input().split()
        y = int(y)
        if x == 'u':
            if current[1]+y < l:
                robloc[1]+=y
                current[1]+=y
            else:
                robloc[1]+=y
                current[1] = l-1
        if x == 'd':
            if current[1]-y >= 0:
                robloc[1]-=y
                current[1]-=y
            else:
                robloc[1]-=y
                current[1] = 0
        if x == 'r':
            if current[0]+y < w:
                robloc[0]+=y
                current[0]+=y
            else:
                robloc[0]+=y
                current[0] = w-1
        if x == 'l':
            if current[0]-y >= 0:
                robloc[0]-=y
                current[0]-=y
            else:
                robloc[0]-= y
                current[0] = 0
    print(f'Robot thinks {robloc[0]} {robloc[1]}')
    print(f'Actually at {current[0]} {current[1]}')
    print()
