from time import sleep
from random import randint
print('|' + '-=-'*10 + '|')
print('|' + '{:=^30}'.format('Sorteio Para a MEGA CENA') + '|')
print('|' + '-=-'*10 + '|')
rsp = int(input('Quantas Jogadas que sortear? '))
nuns = []
sorte = []
for i in range(0, rsp):
    while len(nuns) <= 5:
        n = randint(1, 60)
        if n not in nuns:
            nuns.append(n)
    sorte.append(nuns[:])
    nuns.clear()

for s in sorte:
    s.sort()
    print(f'\n-=--=--=-{sorte.index(s) + 1}° Jogo-=--=--=-')
    print(f'{s}')
    sleep(.5)
