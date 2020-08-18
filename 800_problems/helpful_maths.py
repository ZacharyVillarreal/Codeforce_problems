x = sorted([int(i) for i in input().split('+')])
ans = ''
for i in x:
    ans += str(i) + '+'

print(ans[:-1])
