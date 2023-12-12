tc = int(input())
for _ in range(tc):
    totaldays, totmon = map(int, input().split())
    daysinmon = [int(i) for i in input().split()]
    total = 0
    weekday = 0
    for days in daysinmon:
        if (weekday+13)%7==6 and days>12:
            total+=1
        weekday=(weekday+days)%7
    print(total)
