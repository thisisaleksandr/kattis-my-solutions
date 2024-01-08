while True:
    try: 
        m,p,l,e,r,s,n = map(int, input().split())
        total = m
        for _ in range(n):
            total = p//s
            p = l//r
            l = m*e
            m = total
        print(total)
    except:
        break