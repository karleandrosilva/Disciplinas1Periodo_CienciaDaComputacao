# Crie uma lista de salários de funcionários. Calcule o imposto de renda para cada funcionário na lista

def calculo(salario):
    if salario >= 1.500:
        imposto = 0.27 * salario
        return round(imposto,2)
    else:
        return 0

lista_sal= [
1.500,
2.500,
500
]
for salario in lista_sal:
    imposto = calculo(salario)
    print('salario: {}\nimposto: {}'.format(salario, imposto))


