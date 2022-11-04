from random import randint
from time import sleep
n = randint(1, 10)
print("""
\033[33m{}\033[m
\033[1;46m                 Jogo do Adivinhe o Número                   \033[m
    \033[1;34mSerá que você concegue adivinhar o número em que pensei ?\033[m
                        \033[4;34m(de 1 á 10)
\033[33m{}\033[m
""".format('-=-'*21, '-=-'*21))
i = 1
erro = 0
while True:
    print(f'---------{i}° Chance---------')
    r = int(input('\033[1;34mEm qual número eu Pensei ? '))
    print('PROCESSANDO ...')
    sleep(1.5)
    if r == n:
        print(f'\033[1;32mPARABÉNS, você Venceu meu Jogo na {i}° Tentativa, Seu prêmio é ...')
        sleep(3)
        print('NADA\033[m')
        break
    else:
        erro += 1
        if r < n and erro < 3:
            print('Dica -> MAIS ...')
        elif r > n and erro < 3:
            print('Dica -> MENOS ...')
        print('\033[1;31mVOCÊ ERROU, PERDEDOR!!!\033[m\n'.format(n, r))
    if erro == 3:
        print('\033[1;31mVocê Atingio o Limite máximo de erros, Eu tinha pensado no {}\nVocê é um SUPREMO PERDEDOR !!!\033[m\n'.format(n))
        break
    i += 1
