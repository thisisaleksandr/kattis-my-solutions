m, n = map(int, input().split())
jobs = {}
for _ in range(m):
    pos = input().split()
    jobs[pos[0]] = int(pos[1])
for _ in range(n):
    words = input().split()
    while words[-1] != '.':
        words += input().split()
    counter = 0
    for word in words:
        if word in jobs:
            counter+=jobs[word]
    print(counter)