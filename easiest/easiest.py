def sumnum(number):
    counter = 0
    for num in str(number):
        counter+=int(num)
    return counter


while True:
    n = int(input())
    if n==0:
        break
    for i in range(100000):
        if sumnum(n*i)==sumnum(n) and i>10:
            print(i)
            break