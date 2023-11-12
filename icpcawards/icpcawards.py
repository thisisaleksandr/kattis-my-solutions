num = int(input())
lst = []
counter = 0
while counter !=12:
    univ = input().split()
    if univ[0] not in lst:
        print(*univ)
        counter+=1
    lst.append(univ[0])