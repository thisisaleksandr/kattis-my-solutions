n, m = map(int, input().split())

connected = set()

temp = []

for _ in range(m):
    a, b = map(int, input().split())
    if a==1 or b==1:
        connected.add(a)
        connected.add(b)
    elif a in connected or b in connected:
        connected.add(a)
        connected.add(b)
    else:
        temp.append((a, b))

i = 0

while i < len(temp):
    if temp[i][0] in connected or temp[i][1] in connected:
        connected.add(temp[i][0])
        connected.add(temp[i][1])
        del temp[i]
        i = 0
    else:
        i+=1

if len(connected)==n:
    print("Connected")
else:
    for j in range(2, n+1):
        if j not in connected:
            print(j)
