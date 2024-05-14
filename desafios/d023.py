#leia um número de 0 a 999 e mostre na tela cada um dos digitos separados
#ex 1834 -> 4unidade 3dezenas 8centenas 1milhar
#tentar fazer como string e tentar matemáticamente

num = int(input('Escreva um número de 0 a 999: '))

cent = int(num/100)
res = int(num%100)
dez = int(res/10)
res = int(num%10)
uni = int(res)

print(f'O número {num} tem {cent} centenas, {dez} dezenas e {uni} unidades')

'''----------------------------------------------------------------------------------------'''

num1 = input('Escreva um número: ')
print(f'{num1} tem {num1[0]} centenas, {num1[1]} dezenas e {num1[2]} unidades')