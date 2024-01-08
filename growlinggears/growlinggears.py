def root(a, b, c):
    r = -a * (b/(2*a))**2 + b * (b/(2*a)) + c
    return r

testcs = int(input())
for _ in range(testcs):
    dic = {}
    n = int(input())
    for i in range(1, n+1):
        a, b, c = map(int, input().split())
        dic[i] = root(a, b, c)
    print(max(dic.items(), key=lambda x: x[1])[0])