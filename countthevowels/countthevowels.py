n = input().lower()
c = 0
for i in range(len(n)):
    if n[i] in "aeiou":
        c+=1
print(c)