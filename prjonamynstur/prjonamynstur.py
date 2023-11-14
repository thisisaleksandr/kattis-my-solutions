a, b = map(int, input().split())
dic = {".": 20, "O": 10, '\\': 25, "/": 25, "A": 35, "^": 5, "v": 22}
counter = 0
for _ in range(a):
    for x in input():
        counter+=dic[x]
print(counter)