text = input()
lenstr = int(len(text)/2)
str1 = text[0:lenstr]
str2 = text[lenstr:]
counter1 = 0
counter2 = 0
for k in str1:
    counter1 += (ord(k)-65)

for j in str2:
    counter2 += (ord(j)-65)
    
newstr1=""
newstr2=""
while counter1>26:
    counter1-=26
while counter2>26:
    counter2-=26

for m in str1:
    if ord(m) + counter1 <= 90:
        newstr1+=chr(ord(m)+counter1)
    else:
        newstr1+=chr(ord(m)+counter1-26)
for n in str2:
    if ord(n) + counter2 <= 90:
        newstr2+=chr(ord(n)+counter2)
    else:
        newstr2+=chr(ord(n)+counter2-26)

newstr3 = ""
for z in range(len(newstr1)):
    if ord(newstr1[z]) + ord(newstr2[z])-65 <= 90:
        newstr3+= chr(ord(newstr1[z]) + ord(newstr2[z])-65)
    else:
        newstr3+=chr(ord(newstr1[z]) + ord(newstr2[z])-65-26)
print(newstr3)