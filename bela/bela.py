a = input().split()
num = int(a[0])
b = a[1]
counter = 0
dic = {"A":11, "K":4, "Q":3, "J":2, "T":10, "9":0, "8":0, "7":0}
for _ in range(num*4):
    k = input()
    char = k[0]
    value = k[1]
    if value == b:
        if char == "J":
            counter += 20
        elif char == "9":
            counter += 14
        else:
            counter+=dic[char]
    else:
        counter+=dic[char]
print(counter)  