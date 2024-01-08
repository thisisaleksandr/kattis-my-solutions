num = int(input())
str = input()

lst = []

for i in range(len(str)):
    num = ""
    if str[i].isdigit():
        while str[i].isdigit():
            num += str[i]
            if i != len(str)-1:
              i += 1
            else:
              break
        lst.append(int(num))

print(max(lst))