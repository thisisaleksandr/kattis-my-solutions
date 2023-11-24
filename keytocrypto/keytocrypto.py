cipher = input()
key = input()
word = ''

for i in range(len(cipher)):
    letter = chr(((ord(cipher[i])-65)+26-(ord(key[i])-65))%26 + 65)
    word = word + letter
    key = key + letter
    
print(word)