num = int(input())

a = 1
b = 0

for _ in range(num):

    tempB = b
    b = 0
    b += (a + tempB)
    a = 0
    a += tempB
    
print(a, b)  