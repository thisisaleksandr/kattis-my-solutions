message = input()
key = input()
result = ''
for i in range(len(message)):
    if i%2==0:
        result += chr(((((ord(message[i])-65)+26)-(ord(key[i])-65))%26)+65)
    else:
        result += chr(((((ord(message[i])-65)+26)+(ord(key[i])-65))%26)+65)
print(result)