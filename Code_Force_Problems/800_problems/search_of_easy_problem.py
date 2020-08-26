s = int(input())

x = sum([int(i) for i in input().split()])

if x > 0 :
    print('HARD')
else:
    print('EASY')