def func(lst):
    mini = min(lst)
    string = ''
    for num in lst:
        string+=str(num-mini)
    return string
    

c, p = map(int, input().split())
lst = [int(i) for i in input().split()]
dic = {1: ['0000', '0'], 2: ['00'], 3: ['001', '10'], 4:['01', '100'], 
        5: ['101', '000', '01', '10'], 6: ['000', '00', '011', '20'], 7: ['000', '00', '110', '02']}
counter = 0


    
for i in range(c):
    for case in dic[p]:
        leng = len(case)
        if i+leng<=c:
            if func(lst[i:i+leng]) == case:
                counter+=1
print(counter)