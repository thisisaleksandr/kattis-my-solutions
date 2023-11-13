num = int(input())
dic = {}
for _ in range(num):
    res1 = input()
    dic[res1] = dic.get(res1, 0) + 1
    
dic2 = {}

for _ in range(num):
    res2 = input()
    dic2[res2] = dic2.get(res2, 0) + 1

counter = 0

for keys in dic:
  if keys in dic and keys in dic2:
    counter+=min(dic[keys], dic2[keys])

print(counter)