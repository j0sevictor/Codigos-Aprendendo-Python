from random import randint
print("""
\033[33;46m{}\033[m
\033[1;46m                     Jogo: Par ou ÍMPAR                        \033[m
\033[1;34;46m     Será que você concegue me vencer neste Jogo ?             \033[m
\033[33;46m{}\033[m
""".format('-=-'*21, '-=-'*21))
i = 0
while True:
    i += 1
    print('\033[33m~'*25)
    print(f'\033[1;34m-------{i}° Rodada-------')
    print('\033[33m~\033[m'*25)
    ru = ''
    while '2' != ru != '1':
        ru = input('Digite: [1]-Para PAR\n        [2]-Para ÍMPAR\nEscolha AQUI: ')
        if ru != '1' and ru != '2':
            print('\033[31;1mOPÇÃO INVÁLIDA!!!\033[m')
    while True:
        nu = int(input('Agora digite seu Número: '))
        if nu < 0:
            print('\033[31;1mVALOR INVÁLIDO, APENAS NÚMEROS NATURAIS!!!\033[m')
        else:
            break
    nc = randint(1,100)
    t = nc + nu
    if t % 2 == 0 and ru == '1':
        print(f'\033[32;1mVocê Ganhou, Eu escolhi o Número {nc} que somado com o seu {nu} dá {t}\ne {t} é PAR\033[m')
    elif t % 2 == 1 and ru == '2':
        print(f'\033[32;1mVocê Ganhou, Eu escolhi o Número {nc} que somado com o seu {nu} dá {t}\ne {t} é IMPAR\033[m')
    else:
        print(f'\033[31;1mVocê PERDEU, Eu escolhi o Número {nc} que somado com o seu {nu} dá {t}\ne {t} é ', end='')
        print('PAR' if t % 2 == 0 else 'IMPAR')
        print(f'Mas pelo Menos Você Obteve {i -1} VITÓRIAS CONSSECUTIVAS !!')
        break

