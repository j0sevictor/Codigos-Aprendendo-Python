n1 = int(input('Digite o 1° Número: '))
n2 = int(input('Digite o 2° Número: '))
while True:
    r = input('\n\033[1;34mEscolha uma opção:\n [1]-Adição\n [2]-Multiplicação\n [3]-Maior\n [4]-Novos Números\n [0]-Sair do Sistema\n Escolha AQUI: \033[32;1m')
    if r == '1':
        print(f'Sua soma é:\n{n1} + {n2} = {n1 + n2}')
    elif r == '3':
        if n1 == n2:
            print(f'Não existe Valor maior {n1} e {n2} são IGUAIS')
        elif n1 > n2:
            print(f'O valor {n1} é maior que {n2}')
        else:
            print(f'O valor {n2} é maior que {n1}')
    elif r == '2':
        print(f'Sua multiplicação é:\n{n1} x {n2} = {n1 * n2}')
    elif r == '4':
        n1 = int(input('ReDigite o 1° Número: '))
        n2 = int(input('ReDigite o 2° Número: '))
    elif r == '0':
        break
    else:
        print(f'\033[1;31m{r} é uma Opção inválida')