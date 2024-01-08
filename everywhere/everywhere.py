a = int(input())
for i in range(a):
    lst = []
    b = int(input())
    for k in range(b):
        city = input()
        if city not in lst:
            lst.append(city)
    print(len(lst))
