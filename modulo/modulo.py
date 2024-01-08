counter = 0;
set1 = set()
for _ in range(10):
    num = int(input())
    set1.add(num%42)
print(len(set1))