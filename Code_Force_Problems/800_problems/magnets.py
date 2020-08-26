n = int(input())
row =[]
count = 1
for i in range(n):
    row.append(input())
for i in range(n-1):
    if row[i][1] == row[i+1][0]:
        count+=1
print(count)
