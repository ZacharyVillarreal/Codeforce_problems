s = input()
string = str(s.count('4') + s.count('7'))


if (string.count("4") + string.count("7")) == len(string):
    print('YES')
else:
    print('NO')
