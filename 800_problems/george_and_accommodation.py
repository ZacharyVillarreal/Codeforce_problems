rooms = int(input())
can_live = 0

for i in range(rooms):
    s = [int(i) for i in input().split()]
    if (s[1] - s[0]) >= 2:
        can_live += 1

print(can_live)
