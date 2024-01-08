a = int(input())
c = bin(a).replace("0b", "")
k = int(str(c)[::-1], 2)
print(k)