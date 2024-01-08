text = input()
c=0
lc=0
uc=0
trash=0
for x in text:
    if x=="_":
        c+=1
    else:
        if x.islower()==True:
            lc+=1
        elif x.isupper()==True:
            uc+=1
        else:
            trash+=1
print(c/len(text))
print(lc/len(text))
print(uc/len(text))
print(trash/len(text))