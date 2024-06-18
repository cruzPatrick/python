#leia dois numeros int e compare-os, mostrnado na tela uma mensagem: -O primeiro valor é maior, -O segundo valor é maior, - Não existe valor maior, os dois são iguais

n1 = int(input('Escreva um número inteiro: '))
n2 = int(input('Escreva outro número inteiro: '))

if n1==n2:
    print('Os dois valores são iguais')
elif n1>n2:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')