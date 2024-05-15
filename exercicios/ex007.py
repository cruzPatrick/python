tempo = int(input('Quantos anos tem seu carro? '))

if tempo<=3:
    print('Seu carro é novo')
else:
    print('Seu carro é antigo')
print('--- FIM ---')

print('carro novo' if tempo<=3 else'carro velho')