num = input()

length = len(num)

col = 2**length

x = 0
y = 0

for i in num:
  number = int(i)
  x*=2
  y*=2
  if number==1 or number==3:
    x+=1
  if number==2 or number==3:
    y+=1
  
print(length, x, y)