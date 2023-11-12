a, b = [int(i) for i in input().split()]
shesaw = input()
code = input()
newstr = ''

for k in shesaw:
    newstr+=k

for i in range(1, b-a+1): #16-5=11 , 1-10
    num = ord(newstr[-i])-97
    num2 = ((ord(code[b-i])-97+26-num)%26)+97
    newstr = chr(num2) + newstr
print(newstr)