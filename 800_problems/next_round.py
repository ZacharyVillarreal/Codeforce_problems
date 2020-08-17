z = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]

total_passed = 0


for i in s:
    if i >= s[z[1]-1] and i > 0:
        total_passed += 1

print(total_passed)