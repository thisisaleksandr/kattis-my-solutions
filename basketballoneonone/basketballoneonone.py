text = input()
flag = 0
a = 0
b = 0
for i in range(len(text)-1):
    if text[i]=="A":
            a += int(text[i+1])
    if text[i]=="B":
            b+= int(text[i+1])
    if (a >=11 or b>=11) and flag==0:
        break
    if a==10 and b==10 and flag==0:
        flag = 1
    if flag==1:
        if a>=b+2:
            print("A")
            break 
        if b>=a+2:
            print("B")
            break 
if flag==0:
    if a>b:
        print("A")
    else:
        print("B")