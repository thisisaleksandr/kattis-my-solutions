from math import pi

cases = int(input())
for _ in range(cases):
    r, polyg = map(int, input().split())
    req_len = 2*pi*r
    lst_x = []
    lst_y = []
    lst = []
    mylen = 0
    for _ in range(polyg):
        x, y = map(int, input().split())
        lst_x.append(x)
        lst_y.append(y)
    for i in range(1, polyg):
        catet = abs(lst_x[i] - lst_x[i-1])
        catet2 = abs(lst_y[i] - lst_y[i-1])
        hyp = (catet**2 + catet2**2)**0.5
        mylen+=hyp
    mylen+=((abs(lst_x[0] - lst_x[-1]))**2 + (abs(lst_y[0] - lst_y[-1]))**2)**0.5    
    if mylen<req_len:
        print("Not possible")
    else:
        print((mylen-req_len)/mylen)