num = int(input())
string = input()
mypar = {'[': ']', '{': '}', '(': ')'}
stack = []
flag = True

for char in string:
    if char in mypar:
        stack.append(char)
    elif char in mypar.values():
        if not stack or mypar[stack.pop()] != char:
            flag = False
            break

if flag and not stack:
    print("Valid")
else:
    print("Invalid")
