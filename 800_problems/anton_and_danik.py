no_games = int(input())
wins = input()

a_wins = 0
d_wins = 0

for i in wins:
    if i == 'A':
        a_wins += 1
    else:
        d_wins += 1

if a_wins == d_wins:
    print('Friendship')
elif a_wins > d_wins:
    print('Anton')
else:
    print('Danik')