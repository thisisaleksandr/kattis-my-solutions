num, current, previous = map(int, input().split())
jumps = [int(input()) for _ in range(num)]
total = 0
for rec in jumps:
    if rec>current+previous:
        total+=1
        previous = current
        current = rec
print(total)