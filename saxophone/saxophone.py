tc = int(input())

dic = {'c': [2, 3, 4, 7, 8, 9, 10],
       'd': [2, 3, 4, 7, 8, 9],
       'e': [2, 3, 4, 7, 8],
       'f': [2, 3, 4, 7],
       'g': [2, 3, 4],
       'a': [2, 3],
       'b': [2],
       'C': [3],
       'D': [1, 2, 3, 4, 7, 8, 9],
       'E': [1, 2, 3, 4, 7, 8],
       'F': [1, 2, 3, 4, 7],
       'G': [1, 2, 3, 4],
       'A': [1, 2, 3],
       'B': [1, 2]}



for _ in range(tc):
    dic2 = {i: 0 for i in range(1, 11)}
    line = input()
    last_note = []
    for ind in range(len(line)):
        if ind!=0:
            for note in dic[line[ind]]:
                if note not in last_note:
                    dic2[note]+=1
            last_note = dic[line[ind]]
        else:
            last_note = dic[line[ind]]
            for num in dic[line[ind]]:
                dic2[num]+=1
    print(*dic2.values())
    