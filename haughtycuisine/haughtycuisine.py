n = int(input())
menu = [input().split() for _ in range(n)]
print(*menu[0], sep='\n')