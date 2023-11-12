num = int(input())
for _ in range(num):
    word = input()
    sqr = int(len(word)**0.5)
    for i in range(0, sqr):
        for j in range(0, sqr):
            print(word[((sqr-i-1)+sqr*j)], end = "")
    print()