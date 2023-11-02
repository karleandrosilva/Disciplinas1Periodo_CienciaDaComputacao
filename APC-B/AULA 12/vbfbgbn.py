m = 3
n = 3
a = [0] * n

for i in range(m):
    a[i] = [0] * m

for i in range(m):
    for j in range(n):
        print(a[i][j], end= ' ')
    print()
