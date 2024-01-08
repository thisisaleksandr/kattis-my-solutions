num_stud = int(input())
names = [input() for _ in range(num_stud)]
stud_dic = {name: 0 for name in names}
num_clas = int(input())
attend = [input().split()[1:] for _ in range(num_clas)]

for clas in attend:
    for name in clas:
        stud_dic[name] += 1

for x in sorted(stud_dic.items(), key=lambda x: x[1])[::-1]:
    print(x[1], x[0])