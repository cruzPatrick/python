#leia duas notas e faça a media, se media <5=reprovado, se media entre 5 e 6.9 recuperação, se media>=7 aprovado

n1 = float(input('Escreva a primeira nota: '))
n2 = float(input('Escreva a segunda nota: '))
med=(n1+n2)/2
if med>=7:
    print('Aprovado')
elif med<7 and med>=5:
    print('Recuperação')
else:
    print('Reprovado')