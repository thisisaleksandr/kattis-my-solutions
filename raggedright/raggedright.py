text = []

while True:
    try:
        text.append(input())
    except:
        break

longest = len(max(text, key=len))
total = 0
for line in text[:-1]:
    if len(line) != longest:
        total += (longest - len(line))**2
print(total)