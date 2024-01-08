k = 1
while True:
    num = int(input())
    lst = []
    lst2 = []
    if num!=0:
        for i in range(num):
            word = input()
            if i%2==0:
                lst.append(word)
            else:
                lst2.append(word)
        print("SET", k)
        for name2 in lst:
            print(name2)  
        lst2.reverse()
        for name in lst2:
            print(name)
        k+=1
    else:
        break