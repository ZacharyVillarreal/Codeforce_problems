n = int(input())

print('I become the guy.' if int(input()) == len(set(input().split()[1:] + input().split()[1:])) else 'Oh, my keyboad!')