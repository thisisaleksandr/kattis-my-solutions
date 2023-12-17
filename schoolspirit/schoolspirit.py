def groupscore(scores):
    i = 0
    total = 0
    for ind in scores:
        total += ind * (4/5)**i
        i+=1
    return total/5
students = int(input())
scores = [int(input()) for _ in range(students)]
totalav = 0
for j in range(students):
    totalav += groupscore(scores[0:j] + scores[j+1:])

print(groupscore(scores))
print(totalav/students)