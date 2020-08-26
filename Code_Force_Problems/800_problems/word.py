s = input()
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'

upper_count = 0
lower_count = 0

for i in s:
    if i in uppercase:
        upper_count += 1
    else:
        lower_count += 1

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())