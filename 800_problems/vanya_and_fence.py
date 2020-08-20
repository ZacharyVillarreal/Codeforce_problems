x = [int(i) for i in input().split()]
people_height = [int(i) for i in input().split()]
num_people = x[0]
fence_height = x[1]

width = 0

for i in people_height:
    if i > fence_height:
        width += 2
    else:
        width += 1

print(width)