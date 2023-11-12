num = int(input())
lst = []
lst2 = ["."]
for i in range(num):
    x = input()
    lst.append(x)
    lst2.append(x)
    
counter = 0

for k in range(len(lst2)-1):
    if lst2[k]==lst[k]:
        counter+=1
        
print(counter)