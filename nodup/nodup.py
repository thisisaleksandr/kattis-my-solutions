text = input().split()
lst=[]
for k in text:
    if k not in lst:
        lst.append(k)
if len(lst)!=len(text):
    print("no")
else:
    print("yes")