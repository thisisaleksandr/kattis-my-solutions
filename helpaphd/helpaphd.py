num = int(input())
for _ in range(num):
    text = input()
    if "+" in text:
        print(sum([int(i) for i in text.split("+")]))
    elif "P" in text:
        print("skipped")