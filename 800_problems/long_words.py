no_of_lines = int(input())
for i in range(no_of_lines):
    s = input()
    if len(s) > 10:
        print(s[0] + str(len(s)-2) + s[-1])
    else:
        print(s)

