no_of_rows = 0
no_of_cols = 0

no_of_steps = 0

for i in range(5):
    s = [int(i) for i in input().split()]
    no_of_rows += 1

    if sum(s) == 1:
        no_of_steps += abs(3 - no_of_rows)

        for i in range(5):
            if s[i] == 1:
                no_of_cols = i + 1
        no_of_steps += abs(3 - no_of_cols)
        
print(no_of_steps)
    



