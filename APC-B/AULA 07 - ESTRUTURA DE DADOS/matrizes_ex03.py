def busca(A, valor):
    m = len(A)
    n = len(A[0])
    i = 0
    j = 0
    while i < m:
        while j < n and A[i][j] != valor:
            j+=1
        if j < n:
            return True
        i+=1
        j = 0
    return False
A = [
        [0, -1, 2],
        [3, 1, 5],
        [-4, 0, 6],
        [7, 8, 9]
    ]
print(busca(A, 10))