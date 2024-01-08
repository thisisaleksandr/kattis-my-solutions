tc = int(input())
intervals = [list(map(int, input().split())) for _ in range(tc)]
intervals.sort(key=lambda x: x[1])

maks = 0
last_end = 0
for start, end in intervals:
    if start >= last_end:
        last_end = end
        maks += 1
print(maks)