num = int(input())
lst = []
for i in range(num):
    lst.append(input())
num2 = int(input())
for j in range(num2):
    act = input().split()
    if act[0]=="cut":
        lst.insert(lst.index(act[2]), act[1])
    elif act[0]=="leave":
        del lst[lst.index(act[1])]
for person in lst:
    print(person)