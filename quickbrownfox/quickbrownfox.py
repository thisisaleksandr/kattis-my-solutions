import string

tc = int(input())
alph = string.ascii_lowercase


for _ in range(tc):
    word = input()
    flag = True
    missed = ''
    for letter in alph:
        if letter not in word.lower():
            missed += letter
            flag = False
    if flag:
        print('pangram')
    else:
        print(f'missing {missed}')