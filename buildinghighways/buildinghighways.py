num = int(input())
ways = sorted(list(map(int, input().split())))
mini = ways[0]
counter = 0
for x in ways[1:]:
  counter+=mini+x
print(counter)