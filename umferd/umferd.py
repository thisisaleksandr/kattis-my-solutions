num = int(input())
num2 = int(input())
dots = 0
for _ in range(num2):
    for symb in input():
        if symb==".":
            dots+=1
print(dots/(num*num2))