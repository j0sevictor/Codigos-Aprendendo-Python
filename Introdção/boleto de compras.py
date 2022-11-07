todos = []
i = 0
while True:
    tot = 0
    compra = {'preços': []}
    i += 1
    print('-=-'*4 + f'{i}° Cliente' + '-=-'*4)
    compra['nome'] = str(input('Nome do Cliente: '))
    tp = int(input('Quantos Produtos foram Comprados: '))
    for p in range(0, tp):
        compra['preços'].append(float(input(f'Quanto custou o {p + 1}° Produto: ')))
        tot += compra['preços'][p]
    compra['total'] = 'R$ ' + str(tot)
    todos.append(compra.copy())
    compra.clear()
    while True:
        resp = input('Quer Continuar?[S/N] ').lower().strip()
        if resp in 'ns':
            break
        else:
            print('Resposta Inválida')
    if resp == 'n':
        print()
        break
print()
print('{:-^37}'.format('Tabela de Boletos'))
print('{:^5}|{:^20}|{:^10}'.format('N°', 'Nomes', 'Total'))
for i, e in enumerate(todos):
    print(f'\033[4m{i + 1:^5} {e["nome"]:^20} {e["total"]:<10}\033[m')
while True:
    while True:
        resp = input('\nQuer Ver o Boleto Específico de Alguem?[S/N] ').lower().strip()
        if resp in 'ns':
            break
        else:
            print('Resposta Inválida')
    if resp == 'n':
        print()
        break
    while True:
        r = int(input('Qual o Número dessa Pessoa')) - 1
        if 0 > r or r >= len(todos):
            print('Esse Aluno Não Existe')
        else:
            break
    print('-=-' * 5 + 'Informaçoes Gerais' + '-=-' * 5)
    print(f'Nome: {todos[r]["nome"]}')
    print('Os Preços foram:')
    for p in todos[r]["preços"]:
        print(f'R$ {p}', end=' ')
    print(f'\nTotal: {todos[r]["total"]} ')
    print('-=-' * 5 + 'Informações dos Preços' + '-=-' * 5)
    for pre in todos[r]['preços']:
        print(f'O preço do {todos[r]["preços"].index(pre) + 1}° Produto foi R$ {pre}')
    print(f'E o Total foi de: R$ {todos[r]["total"]}')
