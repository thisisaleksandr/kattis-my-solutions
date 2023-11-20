import time
start_time = time.perf_counter()

n, m = map(int, input().split())

connected = set()

temp = []
que = []

for _ in range(m):
    a, b = map(int, input().split())
    temp.append((a, b))
    if a==1:
        que.append(b)
    elif b==1:
        que.append(a)

for x in que:
    

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

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(elapsed_time)