def go(x, y):   #0,7
    lst = []
    if y-2>=0 and x+1<=7:
        if board[y-2][x+1] != "x":
            board[y-2][x+1] = "x"
            lst.append((x+1, y-2))
    if y+2<=7 and x+1<=7:
        if board[y+2][x+1] != "x":
            board[y+2][x+1] = "x"
            lst.append((x+1, y+2))
    if y-2>=0 and x-1>=0:
        if board[y-2][x-1] != "x":
            board[y-2][x-1] = "x"
            lst.append((x-1, y-2))
    if y+2<=7 and x-1>=0:
        if board[y+2][x-1] != "x":
            board[y+2][x-1] = "x"
            lst.append((x-1, y+2))
    if y-1>=0 and x+2<=7:
        if board[y-1][x+2] != "x":
            board[y-1][x+2] = "x"
            lst.append((x+2, y-1))
    if y+1<=7 and x+2<=7:
        if board[y+1][x+2] != "x":
            board[y+1][x+2] = "x"
            lst.append((x+2, y+1))
    if y-1>=0 and x-2>=0:
        if board[y-1][x-2] != "x":
            board[y-1][x-2] = "x"
            lst.append((x-2, y-1))
    if y+1<=7 and x-2>=0:
        if board[y+1][x-2] != "x":
            board[y+1][x-2] = "x"
            lst.append((x-2, y+1))
    return lst

num = int(input())
for _ in range(num):
    board = [[i for i in range(8)] for _ in range(8)]
    dic = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    turn = input()
    x = dic[turn[0]]
    y = int(turn[1]) - 1    
    y = 7 - y            
    board[y][x] = 'x'   
    counter = 0
    lst = [(x, y)]
    temp = []
    while True:
        lst2 = []
        for z in lst:
            lst2 += go(z[0], z[1])
        if len(lst2) == 0:
            break
        lst = lst2
        temp = lst2
        counter+=1
    
    newlst = []
    for para in temp:
        newlst.append((list(dic)[para[0]] +  str(8 - para[1])))
    newlst.sort()
    sortedlst = sorted(newlst, key=lambda x: x[1], reverse=True)
    print(counter, *sortedlst, sep=' ')