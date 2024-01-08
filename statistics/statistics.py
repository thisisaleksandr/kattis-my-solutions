i=1
while True:
    try:
        newnum = [int(j) for j in input().split()[1:]]
        print(f'Case {i}:', min(newnum), max(newnum), max(newnum)-min(newnum))
        i+=1
    except:
        break