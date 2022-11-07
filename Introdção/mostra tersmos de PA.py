a1 = int(input('Qual o 1° temo da PA: '))
r = int(input('Qual a Razão da PA: '))
t = 10
i = 0
while True:
    if i == 0:
        print(f'Os 10 primeiros termos de sua PA temo são: ')
    else:
        print(f'Os Próximos {nt} termos de sua PA temo são: ')
    for i in range(i,t + 1):
        print('{} -> '.format(a1 + r*i), end = '')
        i += 1
    print('...')
    resp = ''
    while resp != 's' and resp != 'n':
        resp = input('Quer continuar:[S/N] ').lower()
    if resp == 's':
        nt = int(input('Quantos termos a Mais Você que? '))
        t += nt
    else:
        print('Espero ter ajudado !!')
        break

