num = int(input())
reserve = 0
awake = 0
for lect in input():
    if lect == '1':
        if reserve==0:
            reserve+=2
        elif reserve==1:
            reserve+=1
        awake+=1
    else:
        if reserve>0:
            awake+=1
            reserve-=1
print(awake)