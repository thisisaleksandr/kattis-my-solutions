def coconut_splat(s, p):
    seats = [(i, 2) for i in range(p)]  
    next_index = 0
    while len(seats) > 1:
        next_index = (next_index + s) % len(seats)

        player, life = seats[next_index]
        
        if life == 2: 
            seats[next_index] = (player, 1)
            seats.insert(next_index + 1, (player, 1))
        elif life == 1:  
            seats[next_index] = (player, 0)
            next_index += 1
        else: 
            seats.pop(next_index)
            next_index %= len(seats)
    
    return seats[0][0] + 1  

s, p = map(int, input().split())
print(coconut_splat(s - 1, p))