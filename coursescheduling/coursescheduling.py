from collections import defaultdict 

classes = int(input())
schedule = [input().split() for _ in range(classes)]
mydict = defaultdict(set) 

for name in schedule:
    mydict[name[2]].add(name[0]+name[1])

for course, students in sorted(mydict.items()):
    print(course, len(students))