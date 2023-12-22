num = int(input())
population = sorted(list(map(int, input().split())))
counter = 0
for x in population[:(num//2)+1]:
    counter+=x//2
print(sum(population[(num//2)+1:]) + counter)