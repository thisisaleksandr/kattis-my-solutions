a, b = map(int, input().split())
lst = [input() for _ in range(a)]
words = []

for x in range(b):
    newword = ''
    for y in range(a):
        newword+=lst[y][x]
        if x==0:
            words += [piece for piece in lst[y].split("#") if len(piece)>=2]
    words += [piece for piece in newword.split("#") if len(piece)>=2]

print(sorted(words)[0])