def evaluate(a, b, c):
    signs = ['/', '+', '*', '-']
    flag = False
    for sign in signs:
        if eval(a + sign + b) == int(c):
            flag = True
            print(a+sign+b+'='+c)
        elif eval(b + sign + c) == int(a):
            flag = True
            print(a+'='+b+sign+c)
        if flag:
            break
a, b, c = input().split()
evaluate(a, b, c)