date = input().split()
month = date[0]
day = int(date[1])
if month=='OCT' and day==31:
    print("yup")
elif month=='DEC' and day==25:
    print("yup")
else:
    print("nope")