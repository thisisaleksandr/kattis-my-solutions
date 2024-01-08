position = int(input())
num_ques = int(input())
timer = 210

for _ in range(num_ques):
    answer = input().split()
    sec = int(answer[0])
    letter = answer[1]
    if letter == 'T':
        if sec <= timer:
            position += 1
            if position > 8:
                position -= 8
            timer -= sec
        else:
            print(position)
            break
    elif letter == "N" or letter == "P":
        if sec > timer:
            print(position)
            break
        else:
            timer-=sec