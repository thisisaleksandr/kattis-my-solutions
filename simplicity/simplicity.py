string = input()
dic = {}

for letter in string:
    dic[letter] = dic.get(letter, 0) + 1

counter = 0
while len(dic) > 2:
    minim = sorted(dic.items(), key=lambda x:x[1])[0]
    del dic[minim[0]]
    counter+=minim[1]
print(counter)