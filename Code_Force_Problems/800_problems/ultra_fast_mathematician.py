n1 = input()
n2 = input()

s = ''
for i in range(len(n1)):
    if n1[i] == '1' and n1[i] != n2[i]:
        s += '1'
    elif n2[i] == '1' and n2[i] != n1[i]:
        s += '1'
    else:
        s += '0'

print(s)
