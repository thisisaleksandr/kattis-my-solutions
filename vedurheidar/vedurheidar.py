a = int(input())
b = int(input())
for i in range(b):
    text = input().split()
    if int(text[1]) >= a:
        print(text[0], "opin")
    else:
        print(text[0], "lokud")