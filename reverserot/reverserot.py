def rotate(string, rot):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    rotstr = ''
    for let in string:
        rotstr += alp[(alp.index(let) + rot)%28]
    return rotstr

line = input()
while line != '0':
    rot = int(line.split()[0])
    string = line.split()[1]
    print(rotate(string[::-1], rot))
    line = input()