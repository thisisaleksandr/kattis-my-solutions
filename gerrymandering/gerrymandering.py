num_vot, districts = map(int, input().split())
precincts = [[int(i) for i in input().split()] for _ in range(num_vot)]
dic = {}

def voted(r1, r2):
    return ((r1+r2)//2)+1

total = 0
wa = 0
wb = 0

for res in precincts:
    total += (res[1] + res[2])
    if res[0] not in dic:
        dic[res[0]] = [res[1], res[2]]
    else:
        dic[res[0]][0] += res[1]
        dic[res[0]][1] += res[2]
   
for votes in sorted(dic.items()):
    print(['A', 'B'][votes[1][0]<votes[1][1]], end =" ")
    if votes[1][0] > votes[1][1]:
        winner = votes[1][0] - voted(votes[1][0], votes[1][1])
        wa+=winner
        wb+=votes[1][1]
        print(winner, votes[1][1])
    else:
        winner = votes[1][1] - voted(votes[1][0], votes[1][1])
        wa+=votes[1][0]
        wb+=winner
        print(votes[1][0], winner)
        
print(abs(wa - wb)/total)