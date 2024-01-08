nums = [[int(i) for i in input().split()] for _ in range(3)]

x8 = 8**0.5
x2 = 2**0.5
x5 = 5**0.5
counter = 0
for j in range(1, 9):
    for k in range(3):
        for m in range(3):
            if nums[k][m] == j:
                coor = (k, m)
            if nums[k][m] == j+1:
                coor2 = (k, m)
    if coor[0] == coor2[0]:
        counter+= max(coor[1], coor2[1]) - min(coor[1], coor2[1])
    elif coor[1]==coor2[1]:
        counter+= max(coor[0], coor2[0]) - min(coor[0], coor2[0])
    else:
        if max(coor[0], coor2[0])- min(coor[0], coor2[0])==2 and max(coor[1], coor2[1])- min(coor[1], coor2[1])==2:
            counter += x8
        elif max(coor[0], coor2[0])- min(coor[0], coor2[0])==2 and max(coor[1], coor2[1])- min(coor[1], coor2[1])==1 or max(coor[0], coor2[0])- min(coor[0], coor2[0])==1 and max(coor[1], coor2[1])- min(coor[1], coor2[1])==2:
            counter += x5
        else:
            counter += x2
    
print(counter)