num = int(input())

i = 1
total = 0

while i*(i+1)*(i+2) < num:
    total += 1
    i+=1

print(total)