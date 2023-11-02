print('SOMA MATRIZES')

def inicializar_matriz(m,n):
    a = [0]*m
    b = [[0]*n for i in range(m)]
    return a

def imprimir(a,m,n):
    for i in range(m):
        for j in range(n):
            print(a[i][j], end= ' ')
        print()

def soma(a,b,m,n):
    c = inicializar_matriz(m, n, 0)
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
        return c

a = inicializar_matriz(4,4,1)
b = inicializar_matriz(4,4,2)

imprimir(a, 4, 4)
print('--------')
imprimir(b, 4, 4)
print('--------')
imprimir()