#leia três números e mostre qual é maior e qual é menor

n1 = float(input('Escreva um número: '))
n2 = float(input('Escreva outro número: '))
n3 = float(input('Escreva um terceiro número: '))

'''
n1 n2 n3
   n3 n2
n2 n1 n3
   n3 n1
n3 n1 n2
   n2 n1
'''

if n1>n2>n3:
    print(f'maior = {n1} menor = {n3}')
else:
    if n1>n3>n2:
        print(f'maior = {n1} menor = {n2}')
    else:
        if n2>n1>n3:
            print(f'maior = {n2} menor = {n3}')
        else:
            if n2>n3>n1:
                print(f'maior = {n2} menor = {n1}')
            else:
                if n3>n1>n2:
                    print(f'maior = {n3} menor = {n2}')
                else:
                    if n3>n2>n1:
                        print(f'maior = {n3} menor = {n1}')
                    else:
                        print('Não pode valores repetidos')