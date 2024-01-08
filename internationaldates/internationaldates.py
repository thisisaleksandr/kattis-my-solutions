date = [int(i) for i in input().split('/')]
if date[0] > 12:
    print("EU")
elif date[0]<=12:
    if date[1]>12:
        print("US")
    else:
        print("either")
