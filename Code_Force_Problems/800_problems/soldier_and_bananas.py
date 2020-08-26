s = [int(i) for i in input().split()]
no_ban = s[2]
tot_mon = s[1]
ban_cost = s[0]

tot_cost = 0
for i in range(1, no_ban+1):
    tot_cost += i * ban_cost

if tot_cost < tot_mon:
    print('0')
else:
    print(abs(tot_mon - tot_cost))