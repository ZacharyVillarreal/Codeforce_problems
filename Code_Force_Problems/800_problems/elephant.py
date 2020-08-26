s = int(input())
steps = 0
while s > 0:
    if s >= 5:
        s -= 5
        steps += 1
    elif s == 4:
        s -= 4
        steps += 1
    elif s == 3:
        s -= 3
        steps += 1
    elif s == 2:
        s -= 2
        steps += 1
    else:
        s -= 1
        steps += 1

print(steps)