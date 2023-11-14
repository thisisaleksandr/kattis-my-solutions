num = int(input())
text = input().split()
for word in text:
    if word[0].isupper():
        print(word[0], end = "")
