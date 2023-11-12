num = int(input())
for _ in range(num):
    text = input()
    if "Simon says" in text:
        print(text[11:])