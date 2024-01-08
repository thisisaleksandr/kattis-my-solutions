num = int(input()) #num of grants
line = input()


def eq_check(myline):
    let = myline.count(myline[0])
    myset = set(myline)
    flag = True
    for x in myset:
        if myline.count(x) != let:
            flag = False
            break
    return flag

minus = 0
leng = 0
f = False
while True:
    for k in range(minus+1):
        string = line[k:num-minus+k]
        if eq_check(string)==True:
            leng = len(string)
            f = True
            break
    minus += 1
    if f:
        break
print(leng)