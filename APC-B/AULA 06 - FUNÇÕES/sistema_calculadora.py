import calculadora #as calc
n1 = int(input('INFORME UM NÚMERO: '))
n2 = int(input('INFORME OUTRO: '))
resul1 = calculadora.soma(n1,n2)
resul2 = calculadora.subt(n1,n2)
resul3 = calculadora.mult(n1,n2)
resul4 = calculadora.subt(n1,n2)
resul5 = calculadora.media(n1,n2)
print('--------------------')
print('''     RESULTADO 
SOMA: {}
SUBTRAÇÃO: {}
MULTIPLICAÇÃO: {}
DIVISÃO: {}
MÉDIA: {}'''.format(resul1, resul2, resul3, resul4, resul5))