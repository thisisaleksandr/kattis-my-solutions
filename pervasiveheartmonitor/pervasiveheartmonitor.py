while True:
    try:
        data = input().split()
        name = []
        bpm = []
        for x in data:
            if x.isalpha():
                name.append(x)
            else:
                bpm.append(float(x))
        print(sum(bpm)/len(bpm), *name)
    except:
        break