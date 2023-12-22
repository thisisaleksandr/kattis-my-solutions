tc = int(input())
for _ in range(tc):
    num = int(input())
    cards = [i for i in range(1, num+1)]
    cardorder = []
    for j in range(num, 0, -1):
        cardorder.insert(0, j)
        for k in range(0, j):
            cardorder.insert(0, cardorder.pop())
    print(*cardorder)
        