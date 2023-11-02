pessoas = {'nome': 'Gustavo', 'sexo':'M','idade':23}
for key in pessoas.keys():
    print(key) # vai aparecer os nomes das chaves = nome sexo idade
print('='*30)
for key in pessoas.values():
    print(key) # vai aparecer os itens das chaves = Gustavo M 23
print('='*30)
pessoas['nome'] = 'Leandro' # o item dentro de nome vai ser substituido por Leandro.
pessoas['altura'] = 1.78 # criou uma nova chave com um intem
for key, valor in pessoas.items():
    print(key,'=',valor) # vai aparecer a chave o os itens = nome = Gustavo sexo = M idade = 23

