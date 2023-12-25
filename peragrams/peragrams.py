from collections import Counter

word = input()
counter = Counter(word)

total = 0

for let in counter.values():
    if let%2==1:
        total+=1
if total==0:
    print(0)
else:
    print(total-1)
