n = input()
f=0
c=0
c1=0
f1=0
for i in range(len(n)):
    if n[i]=="(":
        f=1
    if f != 1:
        c+=1
    if f1 == 1:
        c1+=1
    if n[i]==')':
        f1=1
if c==c1:
    print("correct")
else:
    print("fix")