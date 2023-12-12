w, p = map(int, input().split())
locations = list(map(int, input().split()))

myset = set()
myset.add(w)
used = []
used.append(w)

for num in locations:
    myset.add(num)
    for usednum in used:
        myset.add(abs(num-usednum))
    used.append(num)
print(*sorted(list(myset)))