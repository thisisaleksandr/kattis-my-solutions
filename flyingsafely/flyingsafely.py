tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    lst = []
    for _ in range(m):
        a, b = map(int, input().split())
        lst.append((a, b))
    print(n-1)