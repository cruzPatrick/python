#Leia o comprimento de 3 retas e diga se elas podem formar um triangulo ou não

r1 = float(input('Escreva o valor de um reta: '))
r2 = float(input('Escreva o valor de outra reta: '))
r3 = float(input('Escreva o valor de uma terceira reta: '))
r1<r2+r3
r2<r1+r3
r3<r1+r2
if (r1<r2+r3) and (r2<r1+r3) and (r3<r1+r2):
    print('Essas retas formam um triângulo')
else:
    print('Não formam um triângulo')