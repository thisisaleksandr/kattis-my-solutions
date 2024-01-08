a, b = map(int, input().split())
while a!=0 or b!=0:
    if a+b==13:
        print("Never speak again.")
    elif a>b:
        print("To the convention.")
    elif a<b:
        print("Left beehind.")
    elif a==b:
        print("Undecided.")
    a, b = map(int, input().split())