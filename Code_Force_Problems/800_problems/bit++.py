no_of_lines = int(input())
total = 0
for i in range(no_of_lines):
    s = input()
    if '++' in s:
        total += 1
    elif '--' in s:
        total -= 1

print(total)
