a = input()
t=0
c=0
g=0
for l in a:
    if l=='T':
        t+=1
    if l=='C':
        c+=1
    if l=='G':
        g+=1
if c>0 and t>0 and g>0:
    z = min(t, c, g)
    print(t**2+c**2+g**2+z*7)
else:
    print(t**2+c**2+g**2)