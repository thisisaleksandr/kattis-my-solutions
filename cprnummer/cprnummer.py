a = input().split("-")
num1 = a[0]+a[1]
counter = 0
for i in range(10):
    if i<3:
        counter += int(num1[i])*(4-i)
    if i>=3:
        counter += int(num1[i])*(10-i)
    
if counter%11==0:
    print(1)
else:
    print(0)