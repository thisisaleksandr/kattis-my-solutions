import math 

while True:
    lst = []
    try:
        r, x, y = map(float, input().split())
        if x*x+y*y>= r*r:
            print("miss")
        else:
            hyp = (x*x+y*y)**0.5
            h = r - hyp
            segm = r*r*math.acos((r-h)/r) - (r-h)*(2*r*h-h*h)**0.5
            left = math.pi * r * r - segm
            print(max(segm, left), min(segm, left))
    except:
        break