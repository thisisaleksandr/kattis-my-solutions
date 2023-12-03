num = input()
cases = int(input())
for _ in range(cases):
    word = input()
    encoded = ''
    for i in range(len(num)):
        encoded += chr((((ord(word[i])-65)*int(num[i]))%26)+65)
    print(encoded)