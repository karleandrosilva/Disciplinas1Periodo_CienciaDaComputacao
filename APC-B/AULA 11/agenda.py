agenda = {}
sair = False
while not sair:
    nome = input('Informe seu nome: ')
    telefone = input('Informe seu número: ')
    agenda[nome] = telefone
    s = input('Deseja sair [S/N]: ')
    sair = True if s == 's' else False
print(agenda)

nome.pesquisa = input('Digite o nome a ser buscado: ')

def existe(chave):
    chaves = agenda.keys()
    for c in chaves:
        if c == chave:
            return True
    return False

if existe(nome.pesquisa):
    print(nome.pesquisa, agenda[nome.pesquisa])
else:
    print()
    
if nome.pesquisa in agenda:
    print('')
print(nome.pesquisa, agenda[nome.pesquisa])