num = int(input())
counter = 0
for _ in range(num):
    item = input().lower()
    if "rose" in item or "pink" in item:
        counter+=1
if counter==0:
    print("I must watch Star Wars with my daughter")
else:
    print(counter)