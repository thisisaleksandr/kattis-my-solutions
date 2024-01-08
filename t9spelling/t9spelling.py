num = int(input())
dic = {2: "abc", 3: "def", 
        4: "ghi", 5: "jkl", 6: "mno",
        7: "pqrs", 8: "tuv", 9: "wxyz",
        0: " "}
i = 1
for _ in range(num):
    text = input()
    fullnum = '.'
    for let in text:
        for alp in dic:
            if let in dic[alp]:
                adding = str(alp)*(dic[alp].index(let)+1)
                if fullnum[-1] != adding[0]:
                    fullnum+=adding
                else:
                    fullnum = fullnum + " "+adding
    print("Case #"+str(i)+": "+fullnum[1:])
    i+=1