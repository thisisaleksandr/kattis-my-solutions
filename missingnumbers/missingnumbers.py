num = int(input())
numbers = [int(input()) for _ in range(num)]
missing = []
for i in range(1, numbers[-1]):
    if i not in numbers:
        missing.append(i)
if len(missing)!=0:
    for misnum in missing:
        print(misnum)
else:
    print("good job")