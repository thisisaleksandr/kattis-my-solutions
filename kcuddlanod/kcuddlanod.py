a, b = input().split()
a = a[::-1]
b = b[::-1]
newnuma = ''
newnumb = ''
for x in a:
    if x=='5':
        newnuma+='2'
    elif x=='2':
        newnuma+='5'
    else:
        newnuma+=x
for t in b:
    if t=='5':
        newnumb+='2'
    elif t=='2':
        newnumb+='5'
    else:
        newnumb+=t
if int(newnuma) > int(newnumb):
  print(1)
else:
  print(2)