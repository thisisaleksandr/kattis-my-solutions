from collections import Counter

word = input()
leng = len(word)//3

w1 = word[0:leng]
w2 = word[leng:leng*2]
w3 = word[leng*2:]

res = ""
for i in range(leng):
    res += max(Counter(w1[i] + w2[i] + w3[i]).items(), key=lambda x:x[1])[0]
print(res)