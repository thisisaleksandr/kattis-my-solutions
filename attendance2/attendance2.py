num = int(input())
names = [input() for _ in range(num)]
absence = []
for i in range(num-1):
    if names[i+1] != 'Present!' and names[i] != 'Present!':
        absence.append(names[i])
if names[-1] != 'Present!':
    absence.append(names[-1])
if len(absence) != 0:
    print(*absence, sep='\n')
else:
    print("No Absences")