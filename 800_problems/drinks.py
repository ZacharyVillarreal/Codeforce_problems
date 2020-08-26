n = int(input())

nums = [int(i) for i in input().split()]
prop = 0

for i in range(n):
    prop += nums[i] / 100



print(round((prop / n)*100, 12))