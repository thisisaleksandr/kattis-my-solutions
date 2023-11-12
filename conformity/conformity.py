num = int(input())
dic = {}
counter = 0
for _ in range(num):
    courses = "".join(sorted(input().split()))
    dic[courses] = dic.get(courses, 0) + 1

for k in dic.keys():
    if dic[k] == max(dic.values()):
        counter+=dic[k]
print(counter)