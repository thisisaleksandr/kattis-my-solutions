num = int(input())
lst = ['aa', 'ee', 'ii', 'oo', 'uu', 'yy']
while num!=0:
    dic = {}
    for _ in range(num):
        counter = 0
        word = input()
        for vow in lst:
            counter += word.count(vow)
        dic[word] = counter
    maks = sorted(dic.items(), key=lambda x:x[1])[-1][0]
    print(maks)
    num = int(input())
