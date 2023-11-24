num = int(input())
each = 60 * 3.14159265359/28

for _ in range(num):
    aph = input()
    counter = 0
    for i in range(len(aph)-1):
        if aph[i]==" ":
            lt1 = 27
        if aph[i]=="'":
            lt1 = 28
        if aph[i+1]==" ":
            lt2 = 27
        if aph[i+1]=="'":
            lt2 = 28
        if aph[i].isalpha():
            lt1 = ord(aph[i])-64
        if aph[i+1].isalpha():
            lt2 = ord(aph[i+1])-64
        if abs(lt2-lt1) < (28-abs(lt2-lt1)):
            counter += each*abs(lt2-lt1)
        else:
            counter += each*(28-abs(lt2-lt1))
    print((counter/15)+len(aph))