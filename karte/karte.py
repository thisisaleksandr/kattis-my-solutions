text = input()
p = []
k = []
h = []
t = []
f=0
for i in range(len(text)):
    if text[i]=='P':
        if text[i:i+3] not in p:
            p.append(text[i:i+3])
        else:
            print("GRESKA")
            f=1
            break;
    elif text[i]=='K':
        if text[i:i+3] not in k:
            k.append(text[i:i+3])
        else:
            print("GRESKA")
            f=1
            break;
    if text[i]=='H':
        if text[i:i+3] not in h:
            h.append(text[i:i+3])
        else:
            print("GRESKA")
            f=1
            break;
    if text[i]=='T':
        if text[i:i+3] not in t:
            t.append(text[i:i+3])
        else:
            print("GRESKA")
            f=1
            break;
    i += 2
if f==0:
  print(13-len(p), 13-len(k), 13-len(h), 13-len(t))