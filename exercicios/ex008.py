"""
nome = str(input('Qual é seu nome? '))
if nome == 'Patrick':
    print('Que nome feio o seu, viu o bob esponja?')
else:
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}')
"""
n1 = float(input('Qual foi a sua primeira nota? '))
n2 = float(input('Qual foi a sua segunda nota? '))

if (n1+n2)/2<=6:
    print('Você está reprovado')
else:
    print('Você está Aprovado')
print(f'Sua média foi {(n1+n2)/2:.1f}')