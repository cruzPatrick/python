#leia três números e mostre qual é maior e qual é menor

n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int(input('Escreva um terceiro número: '))
#a do professor

#menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3


#maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')







'''
n1 n2 n3
   n3 n2
n2 n1 n3
   n3 n1
n3 n1 n2
   n2 n1

minha versão burra
   
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
'''