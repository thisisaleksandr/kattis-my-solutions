num = int(input())
dic = {}
for _ in range(num):
    text = input().split()
    if text[0].isdigit()==True:
        dic[text[1]] = int(text[0])//2
    else:
        dic[text[0]] = int(text[1])


for key in sorted(dic.items(), key=lambda x: x[1]):
  print(key[0])