n, p, q = map(int, input().split())
cur = (p+q)//n
if cur%2==0:
    print("paul")
else:
    print("opponent")