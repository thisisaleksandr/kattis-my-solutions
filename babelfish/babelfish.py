dic = {}

while True:
    try:
        eng, frgn = input().split()
        dic[frgn] = eng
    except:
      break
        
while True:
    try:
        word = input()
        if word in dic:
            print(dic[word])
        else:
            if word=='':
              break
            print("eh")
    except:
        break
