num = int(input())
for _ in range(num):
    text = input().split()
    name = text[0]
    study = [int(i) for i in text[1].split('/')]
    birth = [int(j) for j in text[2].split('/')]
    courses = int(text[3])
    eligib = 0
    if study[0]>= 2010:
        eligib = 1
    if birth[0]>=1991:
        eligib = 1
    if eligib == 0:
        if courses >= 41:
            eligib = 0
        else:
            eligib = 2
    
    if eligib==1:
        print(name, "eligible")
    elif eligib==0:
        print(name, "ineligible")
    elif eligib==2:
        print(name, "coach petitions")