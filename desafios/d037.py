#Leia um num int qualquer e paça para escolher qual a base de conversão: 1 para bin, 2 para octal, 3 para hex

val = int(input('Escreva um número inteiro: '))
con = int(input('Escolha qual base quer converter. 1 = binário, 2 = octal e 3 = hexadecimal: '))

if con == 0 or con>3 or con<0:
    print('Valor errado, por favor faça de novo')
elif con == 1:
    print(f'O valor {val} em binário é {bin(val)[2:]}')
elif con == 2:
    print(f'O valor {val} em octal é {oct(val)[2:]}')
else:
    print(f'O valor {val} em hexadecimal é {hex(val)[2:]}')

print(f'{val}, {bin(val)[2:]} {oct(val)} {hex(val)}')