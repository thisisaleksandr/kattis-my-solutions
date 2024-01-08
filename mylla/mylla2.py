line1 = input()
line2 = input()
line3 = input()
if line1[0]=='O' and line2[0]=='O' and line3[0]=='O':
    print("Jebb")
elif line1[1]=='O' and line2[1]=='O' and line3[1]=='O':
    print("Jebb")
elif line1[2]=='O' and line2[2]=='O' and line3[2]=='O':
    print("Jebb")
elif line1[0]=='O' and line1[1]=='O' and line1[2]=='O':
    print("Jebb")
elif line2[0]=='O' and line2[1]=='O' and line2[2]=='O':
    print("Jebb")
elif line3[0]=='O' and line3[1]=='O' and line3[2]=='O':
    print("Jebb")
elif line1[0]=='O' and line2[1]=='O' and line3[2]=='O':
    print("Jebb")
elif line1[2]=='O' and line2[1]=='O' and line3[0]=='O':
    print("Jebb")
else:
    print("Neibb")