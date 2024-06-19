#faça i cimputador jogar jokenpô com você
import random
from time import sleep

start = str(input('Vamos jogar? [s/n] '))
print('PROCESSANDO...')
sleep(2)
if start == 's':
    #m_jkp = random.randrange(0,2,1)
    p_jkp = str(input('Escolha pedra(0), papel(1) ou tesoura(2): '))
    m_jkp = 0
    print(m_jkp)
    if p_jkp == str(m_jkp):
        if p_jkp == str(0):
            print('Empate, ambos escolheram pedra')
        elif p_jkp == str(1):
            print('Empate, ambos escolheram papel')
        else:
            print('Empate, ambos escolheram tesoura')
    elif p_jkp == str(0):
        if str(m_jkp) == 1:
            print('Você perdeu a máquina escolheu papel')
        else:
            print('Você ganhou a máquina escolheu tesoura')

    elif p_jkp == str(1):
        if str(m_jkp) == 2:
            print('Você perdeu, a máquina escolheu tesoura')
        else:
            print('Você ganhou, a máquina escolheu pedra')
    else: #(2 tesoura)
        if str(m_jkp) == 0:
            print('Você perdeu, a máquina escolheu pedra')
        else:
            print('Você ganhou, a máquina escolheu papel')
else:
    print('Fechando...')