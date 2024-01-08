s = input()
m = input().split()

lst = []

for word in m:
    flag = True
    for let in word:
        if let in s:
            flag = False
            break
    if flag:
      lst.append(word)
    else:
      lst.append("*"*len(word))
      
print(*lst)