arquivo = open('dados/5notas.txt')
notas = []
for linha in arquivo.readlines():
    linha = linha.replace('\n''') 
    notas.append(float(linha))
    notas[notas] = 

media = sum(notas)/notas
print('notas: ', notas)
print('qtd: ', len(notas))
print('soma: ', sum(notas))
print('media: ', (media))

cont = 0
for nota in notas:
    if nota > media:
        cont += 1
print('numero de notas acima de ')