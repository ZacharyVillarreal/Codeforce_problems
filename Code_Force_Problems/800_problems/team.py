no_of_lines = int(input())
total = 0
for i in range(no_of_lines):
    s = [int(i) for i in input().split()]
    if sum(s) >= 2:
        total += 1
    
print(total)