from datetime import time

degree = input()
newdeg = int(degree[:-1]) + int(degree[-1])/10
for h in range(1, 12):
    for m in range(1, 60):
        if m/5 > h:
            if 5.5*m - 30*h==newdeg:
                print(time.strftime(time(h, m), "%H:%M"))
        else:
            if 360 + 5.5*m - 30*h==newdeg:
                print(time.strftime(time(h, m), "%H:%M"))   