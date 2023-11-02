def inicio():
    print('-'*30)
    print(' '*11,'NOTAS',' '*11)
    print('-'*30)
inicio()
aluno = str(input('Olá, Qual é o seu nome: '))
ab1 = float(input(f'Informe sua nota da AB1: '))
ab2 = float(input(f'Informe sua nota da AB2: '))
def calcular_media():
    if ab1 >= 7 and ab2 >= 7:
        media = (ab1 + ab2) / 2
    elif ab1 < 7:
        reavaliacao1 = float(input(f'{aluno}, como sua nota na AB1 foi menor que 7. Informe sua nota da REAVALIAÇÃO: '))
        if ab1 > ab2:
            media = (ab1 + reavaliacao1) / 2
        elif ab2 > ab1:
            media = (ab2 + reavaliacao1) / 2
        else:
            media = (ab1 + reavaliacao1) / 2
    elif ab2 < 7:
        reavaliacao2 = float(input(f'{aluno}, como sua nota na AB2 foi menor que 7. Informe sua nota da REAVALIAÇÃO: '))
        if ab2 > ab1:
            media = (ab2 + reavaliacao2) / 2
        elif ab1 > ab2:
            media = (ab1 + reavaliacao2) / 2
        else:
            media = (ab1 + reavaliacao2) / 2
    if media >= 7:
        print(f'{aluno}, APROVADO POR MÉDIA [AP]')
    elif media < 5:
        print(f'{aluno}, REPROVADO POR MÉDIA [RP]')
    elif media >= 5 < 7:
        nota_final = float(input(f'{aluno}, como você não atingiu a média miníma. Informe sua nota da FINAL: '))
        media_ponderada = (6 * media + 4 * nota_final) / 10
        if media_ponderada >= 5.5:
            print(f'{aluno}, APROVADO NA FINAL [AF]')
        else:
            print(f'{aluno}, REPROVADO NA FINAL [RF]')
    print(f'A SUA MÉDIA FOI: {media or media_ponderada}')
calcular_media()