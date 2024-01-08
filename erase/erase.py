num = int(input())
line1 = input()
line2 = input()

if num%2==1:
    line1 = line1.replace("1", "x")
    line1 = line1.replace("0", "1")
    line2 = line2.replace("0", "x")
    if line1==line2:
        print("Deletion succeeded")
    else:
        print("deletion failed")
else:
    if line1==line2:
        print("Deletion succeeded")
    else:
        print("deletion failed")