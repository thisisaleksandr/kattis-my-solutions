time = input()
ht = int(time[0])
ho = int(time[1])
mt = int(time[2])
mo = int(time[3])
timelst = [0,0,0,0]
tim1 = {ht:[], ho:[8, 9], mt:[], mo:[8, 9]}
tim2 = {ht:[], ho:[4, 5, 6, 7],
        mt:[4, 5, 6, 7], mo:[4, 5, 6, 7]}
tim3 = {ht:[2], ho:[2, 3, 6, 7], 
        mt:[2, 3, 6, 7], mo:[2, 3, 6, 7]}
tim4 = {ht:[1], ho:[1,3,5,7,9],
        mt:[1,3,5,7,9], mo:[1,3,5,7,9]}

for time in [tim1, tim2, tim3, tim4]:
    if ht in time[ht]:
        print('*',end=" ")
    else:
        print('.',end=" ")
    if ho in time[ho]:
        print('*',end=" ")
    else:
        print('.',end=" ")
    print(' ', end=" ")
    if mt in time[mt]:
        print('*',end=" ")
    else:
        print('.',end=" ")
    if mo in time[mo]:
        print('*')
    else:
        print('.')
