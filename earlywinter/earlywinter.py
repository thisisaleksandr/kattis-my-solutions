n, d = map(int, input().split())
nums = list(map(int, input().split()))
counter = 0
change = False
for gap in nums:
    if gap > d:
        counter+=1
    else:
        change = True
        break
if change:
    print(f"It hadn't snowed this early in {counter} years!")
else:
    print("It had never snowed this early!")