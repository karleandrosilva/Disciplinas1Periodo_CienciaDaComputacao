def quadradoMagico(A):
    n = len(A)
    m = len(A[0])
    soma_magica = 0
    #SOMA LINHAS
    for i in range(m):
        soma = 0
        for j in range(n):
            soma += A[i][j]
        if i == 0:
            soma_magica = soma 
        if soma != soma_magica:
            return False

    # SOMA COLUNAS
    for i in range(n):
        soma = 0
        for j in range(m):
            soma += A[i][j]
            if i == 0:
                soma_magica= soma
        if soma != soma_magica:
            return False

    # SOMA DIAGONAIS
    soma = 0
    for i in range(n):
        soma += A[i][j]
        if soma != soma_magica:
            return False
        i = 0
        j = n - 1
        soma = 0
        for i in range(m):
            soma += A[i][j]
            j += 1
        if soma != soma_magica:
            return False
        return True

A = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

print(quadradoMagico(A))