a, b = [int(i) for i in input().split()]
dic = {}
mq = []
qu = []
counter = 0
fl = 0
for _ in range(a):
    name_st = input().split()
    dic[name_st[0]] = name_st[1]
for _ in range(b):
    look = input().replace(" ", "").split("->")
    per1 = look[0]
    per2 = look[1]
    if dic[per1] == 'm' and dic[per2] == 'u':
        counter = 1
        fl=0
        break
    elif dic[per1] == 'm' and dic[per2] == '?':
        fl = 1
        mq.append(per2)
        if per2 in qu:
            counter = 1
            fl = 0
            break
    elif dic[per1] == '?' and dic[per2] == '?':
        fl = 1
        if per1 in mq and per2 in qu:
            counter = 1
            fl = 0
            break
    elif dic[per1] == '?' and dic[per2] == 'u':
        fl = 1
        qu.append(per1)
        if per1 in mq:
            counter = 1
            fl = 0
            break

if fl==1:
    print("?")
else:
    print(counter)
    