num = input().split()
lst = [int(j) for j in input().split()]
counter = 0
i = 0
while i<len(lst)-1:
    if lst[i+1]>lst[i]:
        counter+=1
    i+=1
print(counter+1)