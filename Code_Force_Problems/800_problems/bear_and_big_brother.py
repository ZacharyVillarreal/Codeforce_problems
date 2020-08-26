x = [int(i) for i in input().split()]

weight1 = x[0]
weight2 = x[1]
years = 0

while weight2 >= weight1:
    years += 1
    weight2 *= 2
    weight1 *= 3


print(years)