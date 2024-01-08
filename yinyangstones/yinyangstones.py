string = list(tuple(input()))

w = string.count('W')
b = string.count('B')

if w==b:
    print(1)
else:
    print(0)