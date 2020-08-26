s = [int(i) for i in input().split()]
tot = s[0]
for i in range(s[1]):
    if tot % 10 == 0:
        tot /= 10
    else:
        tot -= 1


print(int(tot))