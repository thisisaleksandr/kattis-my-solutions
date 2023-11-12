T = int(input())
while T > 0:
    testCase, base, num = map(int, input().split())
    dig = 0
    ssd = 0
    i = 0
    while num > 0:
        dig = num % base
        num = num // base
        ssd += dig * dig
        i += 1
    print(testCase, ssd)
    T -= 1