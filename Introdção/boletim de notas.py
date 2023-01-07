alunos = []
inf = []
nota = []
k = 0

print('-~-'*10)
print('{:=^30}'.format('Escola Baixa Média'))
print('-~-'*10)

while True:
    k += 1
    print(f'-=--=--=-{k}° Aluno-=--=--=-')
    nome = input('Digite seu Nome: ')
    n1 = float(input('Qual foi sua 1° Nota: '))
    n2 = float(input('Qual foi sua 2° Nota: '))
    m = (n2 + n1) / 2
    alunos.append([nome, [n1, n2], m])
    while True:
        resp = input('Quer Continuar?[S/N] ').lower().strip()
        if resp in 'ns':
            break
        else:
            print('Resposta Inválida')
    if resp == 'n':
        print('')
        break

print('{:-^42}'.format('Boletim de Resultados'))
print('{:^4}|{:^12}|{:^8}|{:^15}'.format('N°', 'Nomes', 'Médias', 'Estado'))

for i in alunos:
    print('\033[4;1m{:^4} {:^12} '.format(alunos.index(i) + 1, i[0]), end='')
    print('{:^8.1f} '.format(i[2]), end='')
    if i[2] >= 6:
        print('{:^15}'.format('Aprovado'))
    elif 4 < i[2] < 6:
        print('{:^15}'.format('Recuperação'))
    else:
        print('{:^15}'.format('Reprovado'))

while True:
    resp = int(input('\n\033[mDigite o Número do aluno e saiba a nota dele(a): ')) - 1
    if  0 > resp or resp >= len(alunos):
        print('Esse Aluno Não Existe')
    else:
        print('_'*6 + f'Notas de \033[1m{alunos[resp][0]}\033[m' + '_'*6)
        print(f'As Notas Foram: \n{alunos[resp][1][0]} Na Prova 1 e\n{alunos[resp][1][1]} Na Prova 2')
    while True:
        resp = input('Quer Continuar?[S/N] ').lower().strip()
        if resp in 'ns':
            break
        else:
            print('Resposta Inválida')
    if resp == 'n':
        print()
        break
