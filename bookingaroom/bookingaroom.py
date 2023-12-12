r, n = map(int, input().split())
booked = []
for _ in range(n):
    room = int(input())
    booked.append(room)
flag = 1
for i in range(1, r+1):
    if i not in booked:
        print(i)
        flag=0
        break
if flag:
    print("too late")