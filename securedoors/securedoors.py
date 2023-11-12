num = int(input())
data = []

for _ in range(num):
    text = input().split()
    if text[0] == 'entry':
        if text[1] not in data:
            data.append(text[1])
            print(text[1], "entered")
        else:
            print(text[1], "entered (ANOMALY)")
    elif text[0] == 'exit':
        if text[1] in data:
            del data[data.index(text[1])]
            print(text[1], "exited")
        else:
            print(text[1], "exited (ANOMALY)")