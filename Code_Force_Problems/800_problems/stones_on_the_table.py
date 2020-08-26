no_stones = int(input())
stones = input()

no_removed = 0


for i in range(len(stones)-1):
    if stones[i] == stones[i+1]:
        no_removed += 1

print(str(no_removed))

