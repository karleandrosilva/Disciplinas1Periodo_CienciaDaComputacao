m = 4
n = 4
a = [0] * n

for i in range(m):
    a[i] = [0] * m

for i in range(m):
    for j in range(n):
        if i == j:
            a[i][j] = 1
        else:
            a[i][j] = 0
        print(a[i][j], end= ' ')
    print()

print('-----------------')

# for i in range(n):
#     a[i][i] = -1
#     #print(a[i][j], end= ' ')
# print(a)