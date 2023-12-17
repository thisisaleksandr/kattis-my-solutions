from math import pi
r, c = map(int, input().split())
full = pi*r**2
cheese = pi*(r-c)**2
print((cheese/full)*100)