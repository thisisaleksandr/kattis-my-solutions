i=1
dic = {'A#': "Bb", "C#":"Db", "D#":"Eb", "F#":"Gb", "G#":"Ab"}
while True:
    try:
        nota, tone = input().split()
        if nota in dic:
            print(f'Case {i}: {dic[nota]} {tone}')
            i+=1
        elif nota in dic.values():
            print(f'Case {i}: {list(dic)[list(dic.values()).index(nota)]} {tone}')
            i+=1
        else:
            print(f"Case {i}: UNIQUE")
            i+=1
            
    except:
        break