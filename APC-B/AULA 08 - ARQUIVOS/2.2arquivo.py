arquivo = open('dados/2usuarios.txt')
for linha in arquivo.readlines():
    print(linha.replace('\n',''))
arquivo.close()