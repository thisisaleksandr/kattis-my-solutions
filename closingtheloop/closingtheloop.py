tc = int(input())
for i in range(1, tc+1):
    segm = int(input())
    lengs = input().split()
    dic = {'B': [], 'R':[]}
    for sngl in lengs:
        if sngl[-1]=='B':
            dic['B'].append(int(sngl[:-1]))
        else:
            dic['R'].append(int(sngl[:-1]))
    total = 0

    if len(dic['B']) > 0 and len(dic['R']) > 0:
        minlen = len(min(dic.items(), key=lambda x:len(x[1]))[1])
     
        for j in range(minlen):
            total += sorted(dic['B'], reverse=True)[j]-1
            total += sorted(dic['R'], reverse=True)[j]-1
        print(f'Case #{i}: {total}')
    else:
        print(f'Case #{i}: {0}')