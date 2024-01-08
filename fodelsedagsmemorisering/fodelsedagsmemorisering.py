num = int(input())
allnames = {}
for i in range(num):
    name = input().split()
    if name[2] not in allnames:
        allnames[name[2]] = name[:2]
    else:
        if int(name[1]) > int(allnames[name[2]][1]):
            allnames[name[2]] = name[:2]
print(len(allnames))
for j in sorted(allnames.values()):
    print(j[0])