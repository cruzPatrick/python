import random

alu1 = input('Nome do aluno 1: ')
alu2 = input('Nome do aluno 2: ')
alu3 = input('Nome do aluno 3: ')
alu4 = input('Nome do aluno 4: ')

sorteio = random.choice([alu1, alu2, alu3, alu4])

print(f'O aluno sorteado foi {sorteio}')