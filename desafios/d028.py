#o computador escolhe um número de 0 a 5 e peça ao usuário para descobrir qual o número foi escolhido o programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep
val = random.randrange(0, 5, 1) #o guanabara usou randint
usuval = int(input('Fala um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if val == usuval:
    print('Você acertou o número que o computador pensou')
else:
    print(f'Você errou o número que o computador pensou, a resposta certa era {val}')