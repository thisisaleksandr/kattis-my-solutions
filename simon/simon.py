tc = int(input())
for _ in range(tc):
    text = input()
    if text.startswith('simon says'):
        print(text[11:])
    else:
        print()