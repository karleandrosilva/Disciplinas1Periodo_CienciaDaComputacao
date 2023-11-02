import os

print('Seja bem vindo a agenda telefonica')
print('O que você quer fazer: ')
print('1. buscar contato')
print('2. inserir contato')
print('3. remover contato')
print('4. sair')
opc = int(input('Digite uma opção: '))

if opc == 1:
    nome_buscado = input('Digite o nome do contato: ')
    if os.path.exists('dados/6agenda.txt'):
        arquivo = open('dados/6agenda.txt')
        existe_contato = False
        for linha in arquivo.readlines():
            nome, telefone = linha.replace('\n','').split(',')
            if nome == nome_buscado:
                print(nome,telefone)
                existe_contato = True
        if not existe_contato:
            print('Contato não encontrado')
        arquivo.close()
    else:
        print('agenda sem contatos')

elif opc == 2:
    nome = input('Digite nome do contato: ')
    telefone = input('Digite nome do contato: ')
    if os.path.exists('dados/6agenda.txt'):
        arquivo = open('dados/6agenda.txt','a')
        arquivo.write(nome + ','+telefone+'\n')
        arquivo.close()
    else:
        arquivo = open('dados/6agenda.txt','w')
        arquivo.write(nome + ','+telefone+'\n')
        arquivo.close()
# elif opc == 3:
#     nome




