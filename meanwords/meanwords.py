num = int(input())
lst = [input() for _ in range(num)]
for i in range(len(max(lst, key=len))):
    ascii_val = 0
    count = 0
    for word in lst:
        if i<len(word):
            ascii_val += ord(word[i])
            count+=1
    letter = chr(ascii_val//count)
    print(letter, end="")