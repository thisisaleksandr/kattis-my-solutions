a, b, c = [int(i) for i in input().split()]

lst = []
for _ in range(a):
    string = input()
    lst.append(string)


newlst = [j for j in range(a)]
for _ in range(c):
    ques = input().split()
    num = int(ques[0]) - 1
    ans = ques[1]
    for i in range(len(lst)):
        if i in newlst:
            if lst[i][num] != ans:
                del newlst[newlst.index(i)]

if len(newlst) == 1:
    print("unique")
    print(newlst[0]+1)
else:
    print("ambiguous")
    print(len(newlst))