probl = input().split(";")
counter=0
for k in probl:
    if "-" in k:
        z = k.split('-')
        x = int(z[1])-int(z[0])+1
        counter+=x
    else:
        counter+=1
print(counter)