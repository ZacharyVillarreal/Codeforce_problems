s = [int(i) for i in input().split()]
s_line = [i for i in input()]

no_students = s[0]
time = s[1]
s1 = []

for i in range(no_students):
    s1.append(s_line[i])
for i in range(time):
    j = 0
    while j < len(s1) - 1:
        if s1[j] == 'B' and s1[j+1] == 'G':
            temp = s1[j]
            s1[j] = s1[j+1]
            s1[j+1] = temp
            j += 1
        j += 1


print(''.join(s1))