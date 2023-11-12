while True:
    num = int(input())
    if num == 0:
        break
    
    dic = {}

    for i in range(num):
        dic[i] = int(input())
        
    x = dict(sorted(dic.items(), key=lambda x:x[1]))
    
    lst = []
    for j in range(num):
        lst.append(int(input()))
    
    y = sorted(lst)
    dic2 = {}
    
    z=0
    for v in x.keys():
        dic2[v] = y[z]
        z+=1
    
    xyu = dict(sorted(dic2.items()))
    for zhopa in xyu.keys():
        print(xyu[zhopa])
    print() 