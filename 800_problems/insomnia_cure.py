*k, d = [int(input()) for i in ' '*5]
print(d-sum(all(i%x for x in k) for i in range(1, d+1)))