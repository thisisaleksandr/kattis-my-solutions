lst = []
wordset = set()
while True:
    try:
        lst+=(input().split())
    except:
        break
for x in lst:
    for y in lst:
        if x!=y:
            wordset.add(x+y)
print(*sorted(list(wordset)), sep='\n')