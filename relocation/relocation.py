from math import *
nq = input().split()
n = int(nq[0])
q = int(nq[1])
dic = {}  #comp : loc
comp = [int(i) for i in input().split()]
for z in range(1, len(comp)+1):
    dic[z] = comp[z-1]
for k in range(q):
    mov_dist = [int(j) for j in input().split()]
    req = mov_dist[0]
    if req==1:
        dic[mov_dist[1]] = mov_dist[2]
    if req==2:
        print(abs(dic[mov_dist[1]]-dic[mov_dist[2]]))