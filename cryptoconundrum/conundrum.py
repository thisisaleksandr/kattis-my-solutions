str = input()
c=0
for i in range(len(str)):
    if i%3 == 0 and str[i]!="P":
        c+=1
    if i%3 == 1 and str[i]!="E":
        c+=1
    if i%3 == 2 and str[i]!="R":
        c+=1
print(c)