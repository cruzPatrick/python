#refazer o exercicio 35, mas acrescentando se é equilátero=todos os lados iguais; isósceles=dois lados iguais; escaleno=todos os lados diferentes

reta1 = float(input('Qual o valor da primeira reta? '))
reta2 = float(input('Qual o valor da segunda reta? '))
reta3 = float(input('Qual o valor da terceira reta? '))


if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta2+reta1:
    print('Pode ser um triângulo')
    if reta1==reta2==reta3:
        print('O triângulo é equilátero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print(f'Não é possível fazer um triângulo com esses valores: {reta1}, {reta2} e {reta3}')


'''
reta1<reta2+reta3
reta2<reta1+reta3
reta3<reta2+reta1
'''