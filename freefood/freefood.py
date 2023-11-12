num = int(input())
days = set()
for _ in range(num):
    a, b = [int(i) for i in input().split()]
    for j in range(a, b+1):
        days.add(j)
print(len(days))