n = int(input())
s = input().split()

for i in range(1, n+1):
    print(s.index(str(i)+1))