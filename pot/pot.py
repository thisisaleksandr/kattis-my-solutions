num = int(input())
counter=0
for _ in range(num):
    num = input()
    a = int(num[:-1])
    b = int(num[-1])
    counter+=a**b
print(counter)