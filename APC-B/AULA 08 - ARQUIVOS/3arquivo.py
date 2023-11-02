# ler arquivo
arquivo = open('dados/3identidade.txt','r') # R = LER
usuarios = {}
for linha in arquivo.readlines():
    rg, nome = linha.replace('\n','').split(' ')
    usuarios[rg] = nome
print(usuarios)
arquivo.close()