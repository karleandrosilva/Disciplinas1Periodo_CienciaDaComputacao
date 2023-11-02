# Escreva um programa que possui uma função “maior”, que recebe uma lista e devolve o maior elemento na lista.

def maior (lista):
    max = lista[0]
    for num in lista:
        if num > max:
            max = num
    return max

num = [1,2,3,4,5,6]
print(maior(num))

      