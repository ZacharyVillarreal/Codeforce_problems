no_of_stops = int(input())
lst_of_occ = []
tot_in = 0
for i in range(no_of_stops):
    s = [int(i) for i in input().split()]
    tot_in -= s[0]
    tot_in += s[1]

    lst_of_occ.append(tot_in)

print(max(lst_of_occ))


