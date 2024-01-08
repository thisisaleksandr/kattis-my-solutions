text = [i[0] for i in input().split()]
c1 = 0
for j in text:
    c = 0;
    for k in text:
        if j==k:
            c+=1
    if c>c1:
        c1 = c
print(c1)