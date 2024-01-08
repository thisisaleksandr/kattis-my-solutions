text = input()
f = 1
for j in text:
    c = 0
    for k in text:
        if j==k:
            c+=1
    if c>1 and c%2==0:
        f=0
        break
if f==1:
    print(1)
else:
    print(0)
