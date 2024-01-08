text = input()

vowels = ('a', 'e', 'i', 'o', 'u')
i=0
while i<len(text):
    if text[i] not in vowels:
          print(text[i], end='')
          i+=1
    else:
          print(text[i], end='')
          i+=3