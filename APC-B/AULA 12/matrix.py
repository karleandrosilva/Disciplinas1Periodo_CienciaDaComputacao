m = 4
n = 4
a = [0]*m
#print(a)

for i in range(m):
    a[i] = [0]*n
#print(a)

for i in range(n):
    for j in range(m):
        print(a[i][j], end= ' ')
    print()


'''a[2][1] = 5
a[3][0] = 10
a[1][2] = -1
a[-1][2] = 2
print(a)'''