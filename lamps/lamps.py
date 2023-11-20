h, p = map(int, input().split()) #hoursDay, Price

x = 1
bulb = 60*h*x*p/100000 + 5
lower = 11*h*x*p/100000 + 60
h_counter = 1
life_h_b = 1000
life_h_l = 8000

hx = h * x
while bulb<=lower:
    bulb += 60*h*x*p/100000
    lower += 11*h*x*p/100000
    if (hx)>=life_h_b:
        life_h_b += 1000
        bulb += 5
    if (hx)>=life_h_l:
        life_h_l += 8000
        lower += 60
    hx += h*x
    h_counter+=1
print(h_counter) 