#works on tc1
n, m = map(int, input().split())
while n!=0 and m!=0:
    jack = set()
    for _ in range(n):
        jack.add(input())
    jill = set()
    for _ in range(m):
        jill.add(input())
        
    print(len(jack & jill))
    
    n, m = map(int, input().split())