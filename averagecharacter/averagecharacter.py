word = input()
counter = 0
for letter in word:
    counter += ord(letter)
print(chr(counter//len(word)))